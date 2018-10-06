from conans import ConanFile, CMake

class expected_liteConan(ConanFile):
    name = "expected_lite"
    version = "0.9.0"
    license = "Boost Software License - Version 1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    description = "Expected objects for C++11 and later"
    author = "Karl Wallner <kwallner@mail.de>"
    url = 'git@github.com:kwallner/expected-lite.git'
    scm = { "type": "git", "url": "auto", "revision": "auto" }
    no_copy_source = True

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()
        cmake.test()
        
    def package_info(self):
        self.env_info.expected_lite_DIR = self.package_folder