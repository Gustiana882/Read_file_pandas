import pandas as pd
import function as set

class Read:
	def __init__(self):
		self.message = ""
	def menu(self):
		print(set.default("""
		Menu :
		[1] Read file txt
		[2] Read file excel
		[3] Read file csv
		"""))
		menu = input(set.default("Select menu : "))
		
		if(str(menu)=="1"):
			return self.read_txt()
		elif(str(menu)=="2"):
			return self.read_excel()
		elif(str(menu)=="3"):
			return self.read_csv()
		else:
			set.fail("Menu wrong!")
			self.menu()
			
			
	def read_txt(self):
		set.clear()
		print(set.default("==================== [ Read File Txt ] ====================="))
		print(set.default("""
		Select a read method : 
		[1] read (normal)
		[2] readlines
		"""))
		set.fail(self.message)
		method = input(set.default("entered method selected : "))
		def file():
					try:
						self.path = input(set.default("Select path file txt : "))
						self.file= open(self.path)
					except:
						set.fail("no surc file directory")
						file()
					return self.file
					
		if(str(method)=="1"):
			return file().read()
		elif(str(method)=="2"):
			return file().readlines()
		else:
			self.message = "method wrong!"
			self.read_txt()

			
	def menu_tabel(self, data_tabel):
		set.clear()
		print(set.default("==================== [ Read File Excel ] ====================="))
		print(set.default("""
		Select a read method : 
		[1] read (normal)
		[2] select colum
		[3] select row
		[4] select tabel
		"""))
		set.fail(self.message)
		method = input(set.default("entered selected : "))
		
		if(str(method)=="1"):
			return data_tabel
			
		elif(str(method)=="2"):
				file = data_tabel
				set.success(file)
				return self.col(file)
				
		elif(str(method)=="3"):
				file = data_tabel
				set.success(file)
				return self.row(file)
				
		elif(str(method)=="4"):
			file = data_tabel
			set.success(file)
			return self.tabel(file)
			
		else:
			self.message = "method wrong!"
			self.menu_tabel(data_tabel)
			
	def col(self, file):
			colum = input(set.default("input name colom :"))
			try:
				self.col = file[str(colum)]
			except:
				set.fail("no colum selected!")
				self.col(file)
			return self.col
	def row(self, file):
			rows = input(set.default("input row index : "))
			try:
				self.row = file.iloc[int(rows)]
			except:
				set.fail("no row selected!")
				self.row(file)
			return self.row
	def tabel(self, file):
			row = input(set.default("input row index : "))
			col = input(set.default("input colum name : "))
			try:
				self.tabel = file.loc[int(row)][str(col)]
			except:
				set.fail("no tabel selected")
				self.tabel(file)
			return self.tabel
			
			
	def read_excel(self):
			path = input(set.default("Select path file excel : "))
			try:
					self.file = pd.read_excel(path)
			except:
					set.fail("not file directory selected")
					self.read_excel()
			return self.menu_tabel(self.file)
			
	def read_csv(self):
			path = input(set.default("Select path file excel : "))
			try:
					self.file = pd.read_csv(path)
			except:
					set.fail("not file directory selected")
					self.read_csv()
			return self.menu_tabel(self.file)
		


class Creat:
	def menu(self, array):
		print(set.default("""
		Menu :
		[1] Creat file excel
		[2] Creat file csv
		"""))
		menu = input(set.default("Select menu : "))
		
		if(str(menu)=="1"):
			return self.to_excel(array)
		elif(str(menu)=="2"):
			return self.to_csv()
		else:
			set.fail("Menu wrong!")
			self.menu(array)
			
		
	def to_excel(self, array):
		path = input(set.default("select directory to save : "))
		name = input(set.default("input file name : "))
		df = pd.DataFrame(array)
		df.to_excel(path+name, index=False)
		set.success("File "+name+" save to : "+path+name)

	def to_csv(self, array):
		path = input(set.default("select directory to save : "))
		name = input(set.default("input file name : "))
		df = pd.DataFrame(array)
		df.to_csv(path+name, index=False)
		set.success("File "+name+" save to : "+path+name)

		
					
x = Read()
print(x.menu())	
