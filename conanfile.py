from conans import ConanFile, CMake, tools

class ValuePtrConan(ConanFile):
    name = "value-ptr"
    version = "0.1"
    license = "MIT"
    author = "Bruce Collie (brucecollie82@gmail.com)"
    url = "https://github.com/Baltoli/value_ptr_conan"
    description = "Smart pointer with value copy semantics"
    topics = ("memory", "c++", "smart pointer")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = (
        ("Catch2/2.6.1@catchorg/stable", "private"),
    )

    def source(self):
        self.run("git clone https://github.com/baltoli/value_ptr.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder='value_ptr')
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
    	cmake.install()
