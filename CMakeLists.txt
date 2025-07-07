cmake_minimum_required(VERSION 3.16)

project(Optimiser VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Widgets)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Widgets)

set(PROJECT_SOURCES
        main.cpp

        menu.cpp
        ui_menu.h
        menu.ui

#        linear.cpp
        ui_linear.h
        linear.ui

#        multivariable.cpp
        ui_multivariable.h
        multivariable.ui

#        ga.cpp
        ui_ga.h
        ga.ui

#        constrained.cpp
        ui_constrained.h
        constrained.ui

#        multiobjective.cpp
        ui_multiobjective.h
        multiobjective.ui

#        wing.cpp
        ui_wing.h
        wing.ui

#        manufacturing.cpp
        ui_manufacturing.h
        manufacturing.ui

)

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(Optimiser
        MANUAL_FINALIZATION
        ${PROJECT_SOURCES}
        linear.cpp
        multiobjective.cpp
        manufacturing.cpp
        multivariable.cpp
        wing.cpp
        constrained.cpp
        ga.cpp
    )
# Define target properties for Android with Qt 6 as:
#    set_property(TARGET Optimiser APPEND PROPERTY QT_ANDROID_PACKAGE_SOURCE_DIR
#                 ${CMAKE_CURRENT_SOURCE_DIR}/android)
# For more information, see https://doc.qt.io/qt-6/qt-add-executable.html#target-creation
else()
    if(ANDROID)
        add_library(Optimiser SHARED
            ${PROJECT_SOURCES}
        )
# Define properties for Android with Qt 5 after find_package() calls as:
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
    else()
        add_executable(Optimiser
            ${PROJECT_SOURCES}
        )
    endif()
endif()

target_link_libraries(Optimiser PRIVATE Qt${QT_VERSION_MAJOR}::Widgets)

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
if(${QT_VERSION} VERSION_LESS 6.1.0)
  set(BUNDLE_ID_OPTION MACOSX_BUNDLE_GUI_IDENTIFIER com.example.Optimiser)
endif()
set_target_properties(Optimiser PROPERTIES
    ${BUNDLE_ID_OPTION}
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

include(GNUInstallDirs)
install(TARGETS Optimiser
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

if(QT_VERSION_MAJOR EQUAL 6)
    qt_finalize_executable(Optimiser)
endif()
