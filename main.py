# coding: utf-8
import webapp2
import os
import time
from google.appengine.ext import ndb

class User(ndb.Model):
	name = ndb.StringProperty()

class Article(ndb.Model):
	name =  ndb.StringProperty()
	text = ndb.StringProperty()

class Comment(ndb.Model):
	name =  ndb.StringProperty()
	text = ndb.StringProperty()
	article = ndb.KeyProperty()

class MainHandler(webapp2.RequestHandler):

	def post(self):
		#carrega as variaveis enviadas por POST
		
		operationcount = int(self.request.get("operationcount"))
		workload = self.request.get("workload")
		
		#inicializa as variaveis reads e writes
		
		reads = 0
		writes = 0
		
		#atribui o valor para elas de acordo com o workload, 
		#por exemplo: para 500 operacoes e workload B(50/50), o resultado é 250 escritas e 250 leituras
		
		if(workload == "a"):
			reads = 0.5 * operationcount
			writes = 0.5 * operationcount
		elif(workload == "b"): #elif significa else if
			reads = 0.95 * operationcount
			writes = 0.5 * operationcount
		elif(workload == "c"):
			reads = operationcount
			writes = 0
		elif(workload == "w"):
			reads = 0
			writes = operationcount
			
		#começa a contar o tempo, gravando a hora atual em milisegundos
		t0 = time.clock() 
		
		#for readOperations  in readOperationsRange(1, reads):
		#executa leituras aqui
		
		#for writeOperations  in writeOperationsRange(1, writes):
		#executa escritas aqui
		
		#pára de contar o tempo, subtraindo a hora atual da hora inicial
		total = time.clock() - t0
		self.response.write("Terminado, duracao: " + str(total))

# Workload A: Update heavy workload
# This workload has a mix of 50/50 reads and writes.
# Workload B: Read mostly workload
# This workload has a 95% reads and 5% write mix
# Workload C: Read only
# This workload is 100% read
# Workload W: Write only
# This workload is 100% write

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
