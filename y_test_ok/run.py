"""
# Top-level = RUN APP
#
#\n\n\n"""
# SIMPLE MODULE IMPORT TEST
print(__doc__)
# from asset.basic_class import Basic_Kind
from asset.human_class import Human_Kind
from asset.robot_class import Robot_Kind


def main():
    kay = Human_Kind()
    Jay = Robot_Kind()


if __name__ == '__main__':
    main()
