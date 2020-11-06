""" Save a draft as pdf in Download folder.
"""

from api import *
import clr

clr.AddReference("System")
clr.AddReference("System.IO")
clr.AddReference("Interop.SolidEdge")
clr.AddReference("System.Runtime.InteropServices")

import System.Runtime.InteropServices as SRI
import System

__project__ = "save_pdf"
__author__ = "recs"
__version__ = "0.0.2"
__update__ = "2020-11-06"


def main():
    """Generate PDF document in batch."""
    try:
        application = SRI.Marshal.GetActiveObject("SolidEdge.Application")
        response = raw_input(
            """Would you like to print PDF of your opened documents? (Press y/[Y] to proceed.):\n(Option: Press '*' for processing documents in batch)"""
        )

        if response.lower() in ["y", "yes"]:
            doc = application.ActiveDocument
            save_as_pdf(doc, True)

        elif response.lower() in ["*"]:
            # loop through all the drafts
            documents = application.Documents
            for doc in documents:
                save_as_pdf(doc, False)

        else:
            pass

    except AssertionError as err:
        print(err.args)

    except Exception as ex:
        print(ex.args)

    finally:
        prompt_exit()


if __name__ == "__main__":
    print(
        "%s\n--author:%s --version:%s --last-update :%s\n"
        % (__project__, __author__, __version__, __update__)
    )
    main()
