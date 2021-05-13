import redis
import uuid
import random

class Studiosztaly():

    def __init__(self):
        self.r = redis.Redis(decode_responses=True)

    def clean(self):
        self.r.flushdb()

    def __generate_azon__(self):
        return str(uuid.uuid4())

    def uj_film(self, cim, stilus):
        azon = self.__generate_azon__()
        hossz = random.randint(1, 200)
        if self.r.sismember('film_lista', azon) == 1:
            print('A film már létezik')
        else:
            fil = self.r.pipeline(True, None)
            fil.sadd('film_lista', azon)
            fil.hmset('film_' + azon, {'nev': cim, 'stilus': stilus, 'hossz': hossz})
            fil.execute()
            print(azon)

    def uj_rendezo(self, email, jelszo, nev):
        if self.r.sismember('user_lista', email) == 1:
            print('Létezik már az email')
            return False
        else:
            rend = self.r.pipeline(True, None)
            rend.sadd('user_lista', email)
            rend.hmset('user_' + email, {'jelszo': jelszo, 'nev': nev})
            rend.zadd('zset_rendezett_filmek', {'user_' + email: 0})
            rend.execute()
            return True

    def rendezo_lista(self):
        return self.r.smembers('user_lista')

    def rendezo_leker(self, email):
        return self.r.hgetall('user_' + email)

    def email_kiir(self,nev):
        rendezo_tomb = []
        for i in self.rendezo_lista():
            if nev == self.r.hget('user_'+i, 'nev'):
                rendezo_tomb.append(i)
        return rendezo_tomb;

    def elfelejtett_jelszo(self,email):
        return self.r.hget('user_'+email, 'jelszo')

    def rendezo_nyugdij(self,email):
        rend = self.r.pipeline(True,None)
        rend.delete('user_'+email)
        rend.srem('user_lista',email)
        rend.zrem('zset_rendezett_filmek', 'user_'+email)
        rend.delete('rendezett_'+email)
        rend.execute()

    def film_lista(self):
        return self.r.smembers('film_lista')

    def film_leker(self, azon):
        return self.r.hgetall('film_' + azon)

    def efilm(self,email,filmazon):
        rend=self.r.hget('film_'+filmazon, 'hossz')
        r = self.r.pipeline(True, None)
        r.lpush('rendezett_'+email, 'film_'+filmazon)
        r.hincrby('user_'+email,'rendezett', rend)
        r.zincrby('zset_rendezett_filmek', rend, 'user_'+email)
        r.srem('film_lista',filmazon)
        r.execute()

    def rendezes_szerint(self):
        return self.r.zrevrange('rendezett', 0, -1, withscores=True)

    def rendezett_filmek(self, email):
        return self.r.lrange('rendezett_'+email,0,-1)

    def film_hossz(self, filmazon):
        return self.r.hget('film_'+filmazon, 'hossz')

    def ki_rendezo(self,email):
        return self.r.hget('user_'+email,'nev')

    def filmazon_lekercim(self,nev):
        film_tomb = []
        for i in self.film_lista():
            if nev == self.r.hget('film_'+i,'nev'):
                film_tomb.append(i)
        return film_tomb

    def email_kiir(self,nev):
        rendezo_tomb = []
        for i in self.rendezo_lista():
            if nev == self.r.hget('user_'+i, 'nev'):
                rendezo_tomb.append(i)
        return rendezo_tomb