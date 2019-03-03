from App import Application
import sys

def main():

    app = Application()
    app.gui.setApp(app)
    app.gui.setWindowParts()
    app.openningOperations()
    app.gui.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
