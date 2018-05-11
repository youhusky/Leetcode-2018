class Component(object):
    """docstring for Component"""
    def __init__(self):
        super(Component, self).__init__()
        self.depTable = {}
        self.installed = {}
        


    def processCmd(self,cmd, params):
        check = cmd.upper()

        if check == "LIST":
            self.listInstalled()
        elif check == "DEPEND":
            self.addDep(params[0], params[1:])
        elif check == "INSTALL":
            self.install(params[0])
        elif check == "REMOVE":
            self.removeIrrelevent(params[0])

    def listInstalled(self):
        packages = self.installed.keys()
        packages.sort()

        for p in packages:
            print "\t" + p

    def addDep(self,package, dependencies):
        self.depTable[package] = dependencies

    def install(self,package):
        if package in self.installed:
            print "\t" + package + " is already installed."
            return

        if package in self.depTable:
            for dep in self.depTable[package]:
                self.installRelated(dep)

        self.installed[package] = (self.depTable[package], "irrelevent") if package in self.depTable else ([], "irrelevent")
        print "\tInstalling " + package

    def installRelated(self,package):
        if package in self.installed:
            return

        if package in self.depTable:
            for dep in self.depTable[package]:
                self.installRelated(dep)

        self.installed[package] = (self.depTable[package], "related") if package in self.depTable else ([], "related")
        print "\tInstalling " + package

    def removeIrrelevent(self,package):
        if package not in self.installed:
            print "\t" + package + " is not installed."
            return

        if self.checkDepNeeded(package):
            print "\t" + package + " is still needed."
        else:
            print "\tRemoving " + package
            (deps, installType) = self.installed[package]

            del self.installed[package]

            for dep in deps:
                if not self.checkDepNeeded(package) and dep in self.installed and self.installed[dep][1] == "related":
                    self.removeRelated(dep)

    def removeRelated(self,package):
        if package not in self.installed:
            return

        if not self.checkDepNeeded(package):
            print "\tRemoving " + package
            (deps, installType) = self.installed[package]

            del self.installed[package]

            for dep in deps:
                if not self.checkDepNeeded(package) and dep in self.installed and self.installed[dep][1] == "related":
                    self.removeRelated(dep)

    def checkDepNeeded(self,package):
        needed = False

        for deps, installType in self.installed.values():
            #print installed.values()
            if package in deps:
                needed = True
        return needed

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
m = Component()
for line in li:
    print line
    if line == "END":
        break
    cmd = line.split(' ')
    m.processCmd(cmd[0], cmd[1:])