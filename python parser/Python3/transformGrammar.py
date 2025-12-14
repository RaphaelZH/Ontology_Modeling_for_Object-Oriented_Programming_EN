import sys, os, re, shutil

def main(argv):
    fix("/Users/haozhang/GitHub/Ontology_Modeling_for_Object-Oriented_Programming_EN/python parser/Python3/PythonParser.g4")
    fix("/Users/haozhang/GitHub/Ontology_Modeling_for_Object-Oriented_Programming_EN/python parser/Python3/PythonLexer.g4")

def fix(file_path):
    print("Altering " + file_path)
    if not os.path.exists(file_path):
        print(f"Could not find file: {file_path}")
        sys.exit(1)
    parts = os.path.split(file_path)
    file_name = parts[-1]
    shutil.move(file_path, file_path + ".bak")
    input_file = open(file_path + ".bak",'r')
    output_file = open(file_path, 'w')
    for x in input_file:
        if '!this.' in x:
            x = x.replace('!this.', 'not self.')
        if 'this.' in x:
            x = x.replace('this.', 'self.')
        output_file.write(x)
        output_file.flush()
    print("Writing ...")
    input_file.close()
    output_file.close()

if __name__ == '__main__':
    main(sys.argv)
