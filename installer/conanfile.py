from conans import ConanFile, CMake


class InstallerConan(ConanFile):
    name = "Installer"
    version = "0.1"
    settings = "arch"
    build_requires = "Driver/0.1@user/testing"

    def imports(self):
        self.keep_imports = True
        self.copy("*.h")

    def build(self):
        pass
    
    def package(self):
        self.copy("*.h")


