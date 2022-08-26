# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="AYSAM PDFGen",
    version="1.0",
    description="Generador de reportes de vacaciones a través de ID hecho por los pasantes de la Escuela técnica de la Universidad de Mendoza",
    author="Nicolás Bartolomeo, Alejo Talice, Valentino Moreno",
    author_email="n.bartolomeo@alumno.etec.um.edu.ar",
    url="https://github.com/nicobartok0/AYSAM-pdfgen",
    license="Software Libre",
    scripts=["pdf_app.py"],
    console=["pdf_app.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)