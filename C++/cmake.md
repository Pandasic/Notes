---
title: cmake
tag: [计算机课程学习,C++,]
---
# CMake Tutorial

> cmake 官方教程：[CMake Tutorial — CMake 3.20.1 Documentation](https://cmake.org/cmake/help/v3.20/guide/tutorial/index.html)
>
> github 教程 ：https://github.com/ttroy50/cmake-examples.git

[toc]



## 一般流程

```cmake
# 指定cmake 最小的版本
cmake_minimum_required(VERSION 2.6)
# 项目名称
project(main)
# 寻找可用的库
find_package (Threads)
# 设置包含目录
include_directories($ENV{GTEST_ROOT}/include)
# 设置链接目标的路径
link_directories(/usr/local/lib)
# 添加运行目标
add_executable(main main.cpp)
# 设置链接库
target_link_libraries(main gtest gtest_main) #注意这里
target_link_libraries(main ${CMAKE_THREAD_LIBS_INIT})
```

## 概念

### 就地生成 In-Place Build

在根目录下运行 `cmake .`就地生成产生一个与源代码结构与相同的目录，此时MakeFile和obj文件参杂在普通目录下

### 外部生成 Out-of-Source Build

Out-of-Source 允许创建单独的build文件夹[在文件西永的任意位置],所有临时构建与obj文件将被放置于该目录并保证源文件树的干净。

在build文件夹里运行cmake并保证目标文件夹里有CMakeLists.txt文件

```sh
mkdir build
cd build/
make ..
```



## 特殊常量

|常量|说明|
| ------------------------ | ------------------------------------------------------------ |
| CMAKE_SOURCE_DIR         | The root source directory                                    |
| CMAKE_CURRENT_SOURCE_DIR | The current source directory if using sub-projects and directories. |
| PROJECT_SOURCE_DIR       | The source directory of the current cmake project.           |
| CMAKE_BINARY_DIR         | The root binary / build directory. This is the directory where you ran the cmake command. |
| CMAKE_CURRENT_BINARY_DIR | 当前所在的生成目录                                           |
| PROJECT_BINARY_DIR       | 当前项目的生成目录      |
|PROJECY_NAME|项目的名称|
| CMAKE_INSTALL_PREFIX | Cmake Install 的安装路径(默认为 /usr/local) |
## 基础方法

### cmake_minimum_required 配置cmake最低需求的版本
```cmake
cmake_minimum_required(VERSION XX.XX)
```

### project 设置版本名称 与版号的名字
```cmake
project (projectname VERSION 版本号)
```

### add_executable 指定源文件的生成
```cmake
add_executable(aimname sourcename)
生成目标名称 源文件名称

cmake_minimum_required(VERSION 2.6)
project (hello_cmake)
add_executable(${PROJECT_NAME} main.cpp)
```

### set 创建变量

```cmake
# Create a sources variable with a link to all cpp files to compile
set(SOURCES
	src/Hello.cpp
	src/main.cpp
)

add_executable(${PROJECT_NAME} ${SOURCES})
```

### [file 文件操作命令](#file)

```sh
file(CMD filename params)
```

* WRITE 进行写入操作
* file(GLOB SOURCE "src/*.cpp") 进行正则匹配 将匹配结果存入 SOURCE变量

### tag_include_directories 包含头文件目录

当拥有不同的include文件夹时，使用该函数使编译器包含头文件

编译目标时 使用`-I`来编译 `-I/directory/path`

```CMAKE
target_include_directories(target
	PRIVATE
		${PROJECT_SOURCE_DIR}/include
)
```

`PRIVATE`指定了变量的使用范围

### [add_library 添加库](#add_library)

#### 创建添加静态库

```cmake
add_library(libName STATIC
	src/path
)
#创建lib.a文件
```

#### 创建共享库

```cmake
add_library(libName SHARED
	src/path
)
#创建lib.so文件
```

### 库的别名

```cmake
add_library(hello::library ALIAS hello_library)
```



### target_include_directories 添加填充目录

```cmake
target_include_directories(libname
	PUBLIC
	libdir
)

target_include_directories(hello_library
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)
```

在以下场景使用包含的文件

* 编译一个库
* 编译链接 库的任意其他目标

作用域

* PRIVATE
  * 目录被添加至此目标的包含目录中
* INTERFACE
  * 添加至包含目录与任意与库相连接的库
* PUBLIC
  * 同上 ，包含此库中，也包含任意链接的库

### target_link_libraries 添加共享库

```cmake
add_executable(hello_binary
    src/main.cpp
)

target_link_libraries(hello_binary
    PRIVATE
        hello::library
)
```

### Install 安装

安装位置由 CMAKE_INSTALL_PREFIX 指定 由CCMAKE 或则 

`cmake .. -DCMAKE_INSTALL_PREFIX=/install/location`

文件与库由install函数控制

```sh
# 文件安装 安装到${CMAKE_INSTALL_PREFIX}/bin
install (TARGETS cmake_examples_inst_bin
    DESTINATION bin)
  
# 库的安装 安装到${CMAKE_INSTALL_PREFIX}/lib
install (TARGETS cmake_examples_inst
    LIBRARY DESTINATION lib)
    
# windows下的dll 
install (TARGETS cmake_examples_inst
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin)
    
#头文件安装指令 安装到 ${CMAKE_INSTALL_PREFIX}/include中
install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/
    DESTINATION include)

# 安装conf
install (FILES cmake-examples.conf
    DESTINATION etc)
```

当以root 执行 make install  install_manifest.txt将归root所有

```sh
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib cmake_examples_inst_bin
```

项目代码 尝试运行

如果要为所有用户安装 则在添加 binaries或则libraies前添加

```sh
if( CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT )
  message(STATUS "Setting default CMAKE_INSTALL_PREFIX path to ${CMAKE_BINARY_DIR}/install")
  set(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/install" CACHE STRING "The path to use for make install" FORCE)
endif()
```

如果希望暂存文件用来确认包含的文件 使用DESTDIR

```sh
make install DESTDIR=/tmp/stage
```

将创建${DESTDIR}/${CMAKE_INSTALL_PREFIX}来显示。

不支持卸载target 卸载请看[FAQ](https://cmake.org/Wiki/CMake_FAQ#Can_I_do_.22make_uninstall.22_with_CMake.3F)

### 编译选项

- Release - Adds the `-O3 -DNDEBUG` flags to the compiler
- Debug - Adds the `-g` flag
- MinSizeRel - Adds `-Os -DNDEBUG`
- RelWithDebInfo - Adds `-O2 -g -DNDEBUG` flags

### 设置per-Target C++ 标志?

```
target_compile_definitions(cmake_examples_compile_flags
	PRIVATE EX3
)
```

将在编译目标时添加 -DEX3。如果目标是库并且范围(scope)为Public 或者Interface时，定义也会包含连接在在任意executables中。

对于编译选项 也可以使用 `target_compile_options() `

### 设置默认的C++选项

默认的`CMAKE_CXX_FLAGS`为空或包含对应的标志。

为添加默认的编译选项，可以添加

`set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DEX2" CACHE STRING "Set C++ Compiler Flags" FORCE)`

> CACHE STRING "Set C++ Compiler Flags" FORCE 被用来将变量被设置在 CMakeCache.txt 文件中

与`CMAKE_CXX_FLAGS`相似设置C编译标志为 `CMAKE_C_FLAGS`,设置linker`CMAKE_LINKER_FLAGS`

一旦设置`CMAKE_C_FLAGS`和  `CMAKE_CXX_FLAGS`将设置编译标志/定义为全局的目录或者包含目录。不建议使用此方法在一般用途中，最好使用 `target_compile_definitions`

#### 设置C++11 

CMAKE_CXX_STANDARD
CMAKE_CXX_STANDARD_REQUIRED

 ### find_package() 第三方库

搜索CMake modules 在 `CMAKE_MODULE_PATH`搜寻`FindXXX.cmake`,额外的参数  find_package依赖于你搜寻的模块，通常记录在 FindXXX.cmake 文件。

例子

```
find_package(Boost 1.46.1 REQUIRED COMPOENTS filesystem system)
```

其中

* Boost 为库的名称， 被用在去寻找FindBoost.cmake文件中
* 1.46.1 最低版本
* REQUIRED 模块时必须的，如果找不到则失败
* COMPONENTS  要搜寻的库列表

#### 检测包是否被找到

包含问及那将设置一个变量`XXX_FOUND`用来检查包是否包含于系统。

在这个例子中变量为Boost_FOUND:

```
if(Boost_FOUND)
    message ("boost found")
    include_directories(${Boost_INCLUDE_DIRS})
else()
    message (FATAL_ERROR "Cannot find Boost")
endif()
	
```

#### 其他变量

类似于 `XXX_FOUND` variable,其他变量也可以被设置如

`Boost_INCLUDE_DIRS` boost 头文件目录

### 目标别名/导入目标

CMake 3.5 之后 可以在模块内使用`ALIAS`来应用目标，可以使用`Boost::`来声明子系统

- `Boost::boost` for header only libraries
- `Boost::system` for the boost system library.
- `Boost::filesystem` for filesystem library.

正对导入的目标 可以使用

```
target_link_libraries( third_party_include
      PRIVATE
          Boost::filesystem
  )
```

### 无别名目标

大部分的库都使用引入目标，但是对于没有引入目标的库，可以使用以下变量

- xxx_INCLUDE_DIRS - 指向库的include目录
- xxx_LIBRARY 指向库文件的路径

```
# Include the boost headers
target_include_directories( third_party_include
    PRIVATE ${Boost_INCLUDE_DIRS}
)

# link against the boost libraries
target_link_libraries( third_party_include
    PRIVATE
    ${Boost_SYSTEM_LIBRARY}
    ${Boost_FILESYSTEM_LIBRARY}
)
```

### 使用Clang 编译

用于编译和链接代码的控制选项

CMAKE_C_COMPILE 程序被用来编译C代码

CMAKE_CXX_COMPOLER 程序被用来编译C++代码

CMAKE_LINKER 程序被用来链接二进制文件



通过选项来控制C/C++编译器

```
cmake .. -DCMAKE_C_COMPILER=clang-3.6 -DCMAKE_CXX_COMPILER=clang++-3.6
```



### 编译器编译

cmake是一个元构建系统。可以为其他编译器创建构造文件。

cmake 支持下列编译器

- Borland Makefiles
- MSYS Makefiles
- MinGW Makefiles
- NMake Makefiles
- NMake Makefiles JOM
- Ninja
- Unix Makefiles
- Watcom WMake

下列IDE 自带编译器

- Visual Studio 6
- Visual Studio 7
- Visual Studio 7 .NET 2003
- Visual Studio 8 2005
- Visual Studio 9 2008
- Visual Studio 10 2010
- Visual Studio 11 2012
- Visual Studio 12 2013
- Xcode

下列IDE 需要进行配置

- CodeBlocks
- CodeLite
- Eclipse CDT4
- KDevelop3
- Kate
- Sublime Text 2

指定编译器需要使用-G 参数

```sh
cmake .. -G Ninja
```

### 导入目标第三方库

```cmake
target_link_libraries(imported_targets 
	PRIVATE
	 Boost::filesystem
)
```

> 将自动链接Boost::filesystem 和 Boost::system库 并自动包含Boost库

### C++标准

<<<<<<< HEAD
#### 常规标准



#### 标准



#### 编译预期目标
=======
#### 设置C++标准的常用方法

CMake 尝试使用 `CMAKE_CXX_COMPILER_FLAG`函数去编译程序，并将结果储存在变量中

```cmake
include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
```

上述代码 尝试编译`-std=c++11`并且储存结果在`COMPILER_SUPPORTS_CXX11`之中

`include(CheckCXXCompilerFlag)`告诉CMake 包含该函数使其可以使用

一旦确定是否支持，使用标准CMake方法将标志用于所有目标

```cmake
if(COMPILER_SUPPORTS_CXX11)#
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)#
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
else()
    message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()
```

#### 使用CMAKE_CXX_STANDARD 指定C++标准

> cmake 3.1后支持

`CMAKE_CXX_STANDARD` 变量会影响所有目标的 `CXX_STANDARD`属性

CMAKE_CXX_STANDARD 变量会回落到最近最恰当的版本

 可能会在编译时出现意料之外的错误

#### target_compile_feature 函数

> CMake 3.1 后支持

调用`target_compile_feature`函数将为当前的目标，寻找正确的编译目标。

```cmake
target_compile_feature(hello_cpp11 PUBLIC cxx_auto_type)
```

```cmake
message("List of compile features: ${CMAKE_CXX_COMPILE_FEATURES}")
```

### 分库编译 sublibrary

#### 添加子文件夹 add_subdirectory(directory name)

```cmake
add_subdirectory(sublibrary)
```

#### 引用自子项目文件夹

当使用project () 小黄见项目时，CMake将自动创建一个变量被用来引用项目的细节，这些变量一颗被其他子项目或主项目所引用

```cmake
${sublibrary1_SOURCE_DIR}
${sublibrary2_SOURCE_DIR}
```

| Variable           | Info                                                         |
| :----------------- | :----------------------------------------------------------- |
| PROJECT_NAME       | 当前项目的名称 The name of the project set by the current `project()`. |
| CMAKE_PROJECT_NAME | 最高级项目，即第一个被project复制的项目的名称 the name of the first project set by the `project()` command, i.e. the top level project. |
| PROJECT_SOURCE_DIR | 当前项目的源文件文件夹The source director of the current project. |
| PROJECT_BINARY_DIR | 当前build 文件夹 The build directory for the current project. |
| name_SOURCE_DIR    | 子项目的源头文件夹 The source directory of the project called "name". In this example the source directories created would be `sublibrary1_SOURCE_DIR`, `sublibrary2_SOURCE_DIR`, and `subbinary_SOURCE_DIR` |
| name_BINARY_DIR    | 子项目的二进制文件夹 The binary directory of the project called "name". In this example the binary directories created would be `sublibrary1_BINARY_DIR`, `sublibrary2_BINARY_DIR`, and `subbinary_BINARY_DI` |

#### 仅包含头文件的库

cmake 支持`INTERFACE`	 创建一个无build输出的目标

```
add_library(${PROJECT_NAME} INTERFACE)
```

`INTERFACE`生成满足目标的链接需求 但是不编译其中的目标

#### 从子项目引用库

`target_link_libraries`  可以调用子项目的引用库

```
target_link_libraries(subbinary
	PUBLIC
		sublibrary1
)
```
>>>>>>> 424d8c712cff13661b6868fb02392d9a8e163564

同样 可以创建目标别名来为上下文引用

```
add_library(sublibrary2)
add_library(sub::lib2 ALIAS sublibrary2)

target_link_libraries(subbinary
	sub::lib2
)
```

#### 添加子项目的include文件夹

在cmake v3 后 直接使用target_include_directories()命令 创建库。当子项目的源文件与子库链接，则会自动添加  sublibrary_SOURCE_DIR/inc 文件夹



### configure_file 将文件复制到另一个位置并修改内容

```cmake
configure_file(ver.h.in ${PROJECT_BINARY_DIR}/ver.h)

configure_file(<input> <output> [COPYONLY] [ESCAPE_QUOTES] [@ONLY]               [NEWLINE_STYLE [UNIX|DOS|WIN32|LF|CRLF]])
```

并且替换@VAR 或者 ${VAR}的变量值 未定义的话 则为空字符串 

* COPYONLY：只拷贝文件，不进行任何的变量替换。这个选项在指定了NEWLINE_STYLE选项时不能使用（无效）。
* ESCAPE_QUOTES：躲过任何的反斜杠(C风格)转义。
* @ONLY：限制变量替换，让其只替换被@VAR@引用的变量(那么${VAR}格式的变量将不会被替换)。这在配置${VAR}语法的脚本时是非常有用的。
* NEWLINE_STYLE style：指定输出文件中的新行格式。UNIX和LF的新行是\n，DOS和WIN32和CRLF的新行格式是\r\n。这个选项在指定了COPYONLY选项时不能使用(无效)。

### 使用protobuf更新源文件

> protocol 是谷歌一种串行化协议，使用.proto描述数据 
>
> 通过protobuf  proto 文件可以被转化成源文件

#### protocol 安装

```sh
sudo apt-get install protobuf-compiler libprotobuf-dev
```

#### 常量

* `PROTOBUF_FOUND `
* `PROTOBUF_INCLUDE_DIRS` proto 的 头文件
* `PROTOBUF_LIBRARIES` proto 的库

#### 生成源码

PROTOBUF_GENERATE_CPP(PROTO_SRCS PROTO_HDRS AddressBook.proto)

- PROTO_SRCS - 储存在. pb.cc files.
- PROTO_HDRS- 储存在 .pb.h files.
- AddressBook.proto - The .proto file to generate code from.



### 文件生成

### Option

```cmake
option(<variable> "<help_text>" [value])
```

提供开与关的选择 默认为关



## 函数详解

### file

> 链接:https://blog.csdn.net/fuyajun01/article/details/8880121

```
file(CMD filename params)
```

* file(WRITE filename "message towrite"... )

  WRITE 将一则信息写入文件’filename’中，如果该文件存在，它会覆盖它，如果不存在，它会创建该文件。

* file(APPEND filename "message to write"... )

  APPEND 如同WRITE，区别在于它将信息内容追加到文件末尾。

* file(READ filename variable [LIMIT numBytes] [OFFSEToffset] [HEX])

  READ 会读取文件的内容并将其存入到变量中。它会在给定的偏移量处开始读取最多numBytes个字节。如果指定了HEX参数，二进制数据将会被转换成十进制表示形式并存储到变量中。

* file(<MD5|SHA1|SHA224|SHA256|SHA384|SHA512> filenamevariable)

  MD5, SHA1, SHA224, SHA256, SHA384, 和SHA512 会计算出文件内容对应的加密散列。

* file(STRINGS filename variable [LIMIT_COUNT num]
       [LIMIT_INPUT numBytes] [LIMIT_OUTPUTnumBytes]
       [LENGTH_MINIMUM numBytes] [LENGTH_MAXIMUMnumBytes]
       [NEWLINE_CONSUME] [REGEX regex]
       [NO_HEX_CONVERSION])

  STRINGS 从文件中解析出ASCII字符串列表并存储在变量中。文件中的二进制数据将被忽略。回车符(CR)也会被忽略。也能解析Intel Hex和Motorola S-record文件，这两种文件在读取是会自动转换为二进制格式，可以使用参数NO_HEX_CONVERSION 禁用这种自动转换。LIMIT_COUNT设置可返回的最大数量的字符串。LIMIT_INPUT 设置从输入文件中可读取的最大字节数。LIMIT_OUTPUT设置了存储在输出变量中最大的字节数。 LENGTH_MINIMUM设置了返回的字符串的最小长度。小于这个长度的字符串将被忽略。 LENGTH_MAXIMUM 设置返回的字符串的最大长度。大于这个长度的字符串将被切分为长度不大于于最大长度值的子字符串。NEWLINE_CONSUME 允许换行符包含进字符串中而不是截断它们。REGEX 指定了返回的字符串必须匹配的正则表达式的模式。典型用法

* file(STRINGS myfile.txt myfile)， 将输入文件的每行内容存储在变量"myfile"中。

* file(GLOB variable [RELATIVE path] [globbingexpressions]...)

  GLOB 会产生一个由所有匹配globbing表达式的文件组成的列表，并将其保存到变量中。Globbing 表达式与正则表达式类似，但更简单。如果指定了RELATIVE 标记，返回的结果将是与指定的路径相对的路径构成的列表。 (通常不推荐使用GLOB命令来从源码树中收集源文件列表。原因是：如果CMakeLists.txt文件没有改变，即便在该源码树中添加或删除文件，产生的构建系统也不会知道何时该要求CMake重新产生构建文件。globbing 表达式包括：

     *.cxx     - match all files with extension cxx
     *.vt?      - match all files with extension vta,...,vtz
     f[3-5].txt - match files f3.txt,f4.txt, f5.txt

* file(GLOB_RECURSE variable [RELATIVE path]
       [FOLLOW_SYMLINKS] [globbingexpressions]...)

  GLOB_RECURSE 与GLOB类似，区别在于它会遍历匹配目录的所有文件以及子目录下面的文件。对于属于符号链接的子目录，只有FOLLOW_SYMLINKS指定一或者cmake策略CMP0009没有设置为NEW时，才会遍历这些目录。

  Examples of recursive globbing include:

     /dir/*.py - match all python files in /dir and subdirectories

   

* file(RENAME <oldname> <newname>)

  RENAME 将文件系统中的文件或目录移动到目标位置，并自动替换目标位置处的文件或目录。

* file(REMOVE [file1 ...])

  REMOVE 会删除指定的文件以及子目录下的文件。

* file(REMOVE_RECURSE [file1 ...])

  REMOVE_RECURSE 会删除指定的文件及子目录，包括非空目录。

* file(MAKE_DIRECTORY [directory1 directory2 ...])

  MAKE_DIRECTORY在指定目录处创建子目录，如果它们的父目录不存在，也会创建它们的父目录。

* file(RELATIVE_PATH variable directory file)

  RELATIVE_PAT推断出指定文件相对于特定目录的路径。

* file(TO_CMAKE_PATH path result)

  TO_CMAKE_PATH会将路径转换成cmake风格的路径表达形式。

* file(TO_NATIVE_PATH path result)

  TO_NATIVE_PATH与TO_CMAKE_PATH类似，但执行反向操作，将cmake风格的路径转换为操作系统特定风格的路径表式形式。

* file(DOWNLOAD url file [INACTIVITY_TIMEOUT timeout]
       [TIMEOUT timeout] [STATUS status] [LOGlog] [SHOW_PROGRESS]
       [EXPECTED_MD5 sum])

  DOWNLOAD下载指定URL的资源到指定的文件上。如果指定了LOG 参数，将会把下载的日志保存到相应的变量中。如果指定了STATUS变量，操作的状态信息就会保存在相应的变量中。返回的状态是一个长度为2的列表。第一个元素是操作的返回值。0表示操作过程中无错误发生。如果指定了TIMEOUT，单位于秒，且必须为整数，那么在指定的时间后，操作将会超时，INACTIVITY_TIMEOUT指定了操作在处于活动状态超过指定的秒数后，应该停止。如果指定了EXPECTED_MD5，如果操作会检验下载后的文件的实际md5校验和是否与预期的匹配，如果不匹配，操作将会失败，并返回相应的错误码。如果指定了 SHOW_PROGRESS，那么进度的信息将会被打印成状态信息直到操作完成。

* file(UPLOADfilename url [INACTIVITY_TIMEOUT timeout]
       [TIMEOUT timeout] [STATUS status][LOG log] [SHOW_PROGRESS])

  UPLOAD与DOWNLOAD类似，它执行的是一个上传操作。参数含义与DOWNLOAD 一致。

 

* file(<COPY|INSTALL> files... DESTINATION<dir>
       [FILE_PERMISSIONS permissions...]
       [DIRECTORY_PERMISSIONSpermissions...]
       [NO_SOURCE_PERMISSIONS][USE_SOURCE_PERMISSIONS]
       [FILES_MATCHING]
       [[PATTERN <pattern> | REGEX<regex>]
       [EXCLUDE] [PERMISSIONSpermissions...]] [...])

  COPY表示复制文件，目录以及符号链接到一个目标文件夹中。输入路径将视为相对于当前源码目录的路径。目标路径则是相对于当前的构建目录。复制保留输入文件的一些权限属性，

  除非显式指定了NO_SOURCE_PERMISSIONS（默认是USE_SOURCE_PERMISSIONS），关于文件权限，PATTERN,REGX和EXCLUDE等相关选项可参考install(DIRECTORY)命令的文档。 

  INSTALL 与COPY略微有点不同：它打印状态信息，并且默认情况下指定了 NO_SOURCE_PERMISSIONS。

### [add_library](https://blog.csdn.net/LaineGates/article/details/108242803)

#### normal library

```cmake
add_library(<name> [STATIC | SHARED | MODULE]
            [EXCLUDE_FROM_ALL]
            [source1] [source2 ...])
```

name 为库的名称 源文件可指定 且必须全局唯一

STATIC(静态库)/SHARED(动态库)/MODULE(模块库)

生成的library名会根据STATIC或SHARED成为name.a或name.lib
这里的STATIC和SHARED可不设置，通过全局的BUILD_SHARED_LIBS的FALSE或TRUE来指定
windows下，如果dll没有export任何信息，则不能使用SHARED，要标识为MODULE

添加的库会被输出到以下几个目录
ARCHIVE_OUTPUT_DIRECTORY, LIBRARY_OUTPUT_DIRECTORY和 RUNTIME_OUTPUT_DIRECTORY，详见cmake 常用设定及函数
设置EXCLUDE_FROM_ALL，可使这个library排除在all之外，即必须明确点击生成才会生成

#### imported library

```cmake
add_library(<name> <SHARED|STATIC|MODULE|OBJECT|UNKNOWN> IMPORTED
            [GLOBAL])
```



导入已经生成的库

这种用法的关键在于添加变量`IMPORTED`。另外，`GLOBAL`可用于设置这个library为全局可见。
常规和imported的library的属性不同：

1. 常规的library，其属性以`INTERFACE_`开头
2. imported的library，其属性以`IMPORTED_`开头

alias library（别名库）
为给定library添加一个别名，后续可使用<name>来替代<target>。

add_library(<name> ALIAS <target>)
1
使用有如下限制：

<target>不能是ALIAS
可用于判断target是否存在、链接。
ALIAS的library不能修改属性，不能调用set_property(), set_target_properties()和target_link_libraries()等方法
不能用于install()

#### interface library

创建一个接口库

````c++
add_library(<name> INTERFACE [IMPORTED [GLOBAL]])
````

这类库有属性，能install()，export和imported，但可能没有build过程。像纯头文件库或完全针对target的设计（这条参见interface libraries）
所有INTERFACE _*属性从如下几个方法中设置
set_property()、target_link_libraries(INTERFACE)、target_link_options(INTERFACE)、target_include_directories(INTERFACE)、target_compile_options(INTERFACE)、target_compile_definitions(INTERFACE)和target_sources(INTERFACE)



#### 手工配置库

参考 cmake引入外部库

静态库

```cmake
add_library(baz STATIC IMPORTED)
set_target_properties(baz PROPERTIES
IMPORTED_LOCATION_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/libbaz.a
IMPORTED_LOCATION_DEBUG ${CMAKE_CURRENT_SOURCE_DIR}/libbazd.a)
```

静态库(添加依赖项)

````cmake
add_library(bar STATIC IMPORTED)
set_target_properties(bar PROPERTIES
IMPORTED_LOCATION_RELEASE ${CMAKE_CURRENT_SOURCE_DIR}/libbar.a
IMPORTED_LOCATION_DEBUG ${CMAKE_CURRENT_SOURCE_DIR}/libbard.a
IMPORTED_LINK_INTERFACE_LIBRARIES baz) # <-- dependency is here
````

动态库

````cmake
add_library(bar SHARED IMPORTED)
set_property(TARGET bar PROPERTY IMPORTED_LOCATION c:/path/to/bar.dll)
set_property(TARGET bar PROPERTY IMPORTED_IMPLIB c:/path/to/bar.lib) # 多了lib信息
add_executable(myexe src1.c src2.c)
target_link_libraries(myexe bar)
````

当然，也可以直接引用库文件

```cmake
TARGET_LINK_LIBRARIES(skiaSampleCode
debug skiaCored.lib
optimized skiaCore.lib)
```

#### tag_link_libraries

```cmake
target_link_libraries(<target> ... <item>... ...)
```

### 