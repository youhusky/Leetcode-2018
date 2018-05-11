from sys import *
class Component(object):
	"""docstring for Component"""
	def __init__(self, name):
		super(Component, self).__init__()
		self.name = name
		self.isInstall = False
		self.dependencies = set()
		self.dependents = set()

	def makeDependency(self, component):
		if not component:
			print "Dependency is None"
		self.dependencies.add(component)
		component.dependents.add(self)

	def install(self):
		self.install_helper(self)


	def install_helper(self, component):
		if component.isInstall:
			print "\t" + self.name + " is already installed"
			return

		for comp in component.dependencies:
			print comp.name, comp.isInstall
			if comp.isInstall:
				continue
			comp.isInstall = True
			print "\tInstalling " +comp.name 
		component.isInstall = True
		print "\tInstalling " + component.name 

	def remove(self):
		if self.isInstall == False:
			print self.name + " is not installed"
			return
		self.remove_helper(self,1)

	def remove_helper(self, component, i):
		temp = component.dependencies
		if not component.dependents:
			component.isInstall = False
			print component.name + " uninstalling"
			for comp in component.dependencies:
				#print comp.name + " uninstalling"
				comp.dependents.remove(component)
			component.dependencies = set()
		else:
			if self.name == component.name:
				print component.name + " is still needed"
			return
		for c in temp:
			if i < 2:
				self.remove_helper(c,i+1)

	def listDependency(self):
		print self.name + ":" + str(self.isInstall)
		print "Dependencies:"
		for dependency in self.dependencies:
			print dependency.name + ":" + str(dependency.isInstall)

dic = {}
li = [
"DEPEND TELNET TCPIP NETCARD",
"DEPEND TCPIP NETCARD",
"DEPEND DNS TCPIP NETCARD",
"DEPEND BROWSER TCPIP HTML",
"INSTALL NETCARD",
"INSTALL TELNET",
"INSTALL foo",
"REMOVE NETCARD",
"INSTALL BROWSER",
"INSTALL DNS",
"LIST",
"REMOVE TELNET",
"REMOVE NETCARD",
"REMOVE DNS",
"REMOVE NETCARD",
"INSTALL NETCARD",
"REMOVE TCPIP",
"REMOVE BROWSER",
"REMOVE TCPIP",
"END"]
count = 0
for line in li:
	print line
	line = line.split(' ')
	operater = line[0]
	if operater == "DEPEND":
		globals()['c' + str(count)] = Component(line[1])
		
		dic[line[1]] = 'c' + str(count)
		count += 1
		for each in line[2:]:
			globals()['c' + str(count)] = Component(each)
			dic[each] = 'c' + str(count)
			dic[line[1]].makeDependency(dic[each])
		print dic[line[1]].dependencies
	elif operater == "INSTALL":

		if line[1] in dic:
			dic[line[1]].install()
			print dic[line[1]].dependencies
		else:
			dic[line[1]] = Component(line[1])
			dic[line[1]].install()
		


c1 = Component("C1")
c2 = Component("C2")
c3 = Component("C3")
c4 = Component("C4")
c5 = Component("C5")

c1.makeDependency(c2)
c1.makeDependency(c3)
c2.makeDependency(c3)
c4.makeDependency(c2)
c4.makeDependency(c3)
c5.makeDependency(c2)

print "Before c1 is install"
c1.listDependency()
print ""
c3.install()
print ""
c1.install()
print ""
c3.remove()
print ""
c5.install()
print ""
c4.install()
print ""
c1.remove()
print ""
c3.remove()
print ""
c4.remove()
print ""
c3.remove()
print ""
c3.install()
print ""
c2.remove()
print ""
c5.remove()
print ""
c2.remove()
		