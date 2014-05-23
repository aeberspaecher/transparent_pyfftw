#!/usr/bin/env python
#-*- coding:utf-8 -*-

top = "."
out = "build"


def options(opt):
    opt.load("python")
    opt.add_option("--wisdom-file", action="store", dest="wisdom_file",
                   default="None", help="File to load wisdom from on import")
    opt.add_option("--num-threads", action="store", dest="num_threads",
                   default="1", help="Number of threads")


def configure(conf):
    conf.load("python")
    conf.check_python_version((2, 4))  # TODO: which version do we need here?
    conf.check_python_module("pyfftw")

    num_threads = int(conf.options.num_threads)
    wisdom_file = conf.options.wisdom_file
    option_file_content = """
pyfftw_threads = %s
wisdom_file = '%s'
"""%(num_threads, wisdom_file)
    opt_file = file("options.py", mode="w")
    opt_file.write(option_file_content)
    opt_file.close()


def build(bld):
    bld(features="py", source=bld.path.ant_glob("*.py"),
        install_path="${PYTHONDIR}/transparent_pyfftw")


# TODO: add two options: --num-threads and --wisdom-file
