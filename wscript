#!/usr/bin/env python
#-*- coding:utf-8 -*-

top = "."
out = "build"


def options(opt):
    opt.load("python")
    opt.add_option("--wisdom-file", action="store", dest="wisdom_file",
                   default="None", help="File to load wisdom from on import")


def configure(conf):
    conf.load("python")
    conf.check_python_version((2, 4))  # TODO: which version do we need here?
    conf.check_python_module("pyfftw")

    wisdom_file = conf.options.wisdom_file
    option_file_content = "wisdom_file = '%s'"%(wisdom_file)
    opt_file = file("options.py", mode="w")
    opt_file.write(option_file_content)
    opt_file.close()


def build(bld):
    bld(features="py", source=bld.path.ant_glob("*.py"),
        install_path="${PYTHONDIR}/transparent_pyfftw")
