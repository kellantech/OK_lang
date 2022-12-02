

# python files
echo -n "downloading main.py..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/main.py
echo "done"

echo -n "downloading get_args.py..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/get_args.py
echo "done"

echo -n "downloading parse_if.py..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/parse_if.py
echo "done"

echo -n "downloading parse_var.py..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/parse_var.py
echo "done"

echo -n "downloading parse_func.py..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/parse_func.py
echo "done"

echo -n "downloading cond_eval.py..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/cond_eval.py
echo "done"

echo -n "downloading custom_eval.py..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/custom_eval.py
echo "done"

# standard library 
echo "downloading standart library..."

echo -n "  downloading fs.ok..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/stdlib/fs.ok
echo "done"

echo -n "  downloading io.ok..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/stdlib/io.ok
echo "done"

echo -n "  downloading sys.ok..."
curl -O -s https://raw.githubusercontent.com/kellantech/OK_lang/main/stdlib/sys.ok
echo "done"

echo "done"
# move files
echo -n "creating and moving files..."
mkdir stdlib
mv fs.ok stdlib
mv io.ok stdlib
mv sys.ok stdlib


echo "OKLANG_DIR = "\"$(pwd)\" > OKDIR.py

echo "#!/bin/bash" >> oklang
echo "python3 $(pwd)/main.py \$@" >> oklang

chmod +x oklang

echo "done"


echo "move file oklang to where you want to use OK Lang"
