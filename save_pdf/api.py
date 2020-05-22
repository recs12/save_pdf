"""
Api solidedge
=======================

"""

import clr

clr.AddReference("System")
clr.AddReference("System.IO")
clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import SolidEdgeFramework as SEFramework
import SolidEdgePart as SEPart
import System.Runtime.InteropServices as SRI
import System
from System import Console
from System.Diagnostics.Process import Start
from System.IO.Path import Combine
from System.IO import Directory

def  raw_input(message):
    Console.WriteLine(message)
    return Console.ReadLine()

def is_exist(path_to_check):
    return Directory.Exists(path_to_check)

def makedirs(path_to_make):
    Directory.CreateDirectory(path_to_make)

def userprofile():
    return System.Environment.GetEnvironmentVariable("USERPROFILE")

def username():
    return System.Environment.UserName

def combine(path1, path2):
    return Combine(path1, path2)

def start(path_pdf):
    Start(path_pdf)

class Api:
    def __init__(self):
        # Connect to a running instance of Solid Edge
        self.api = SRI.Marshal.GetActiveObject("SolidEdge.Application")

    def check_valid_version(self, *valid_version):
        # validate solidedge version - 'Solid Edge ST7'
        print("version solidedge: %s" % self.api.Value)
        assert self.api.Value in valid_version, "Unvalid version of solidedge"

    def active_document(self):
        return self.api.ActiveDocument

    def open_document(self, path_to_item):
        return self.document.Open(path_to_item)

    def close_document(self):
        return self.document.Close()
