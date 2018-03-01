from conans import ConanFile, CMake


class DriverConan(ConanFile):
    name = "Driver"
    version = "0.1"
    settings = "arch"
   
    exports_sources = "src/*"

    def package(self):
        self.copy("*32.h", dst="include", src="src")
        if self.settings.arch == "x86_64":
            self.copy("*64.h", dst="include", src="src")
