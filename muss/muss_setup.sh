pip install -r requirements.txt
git clone git@github.com:facebookresearch/muss.git
cd muss/
pip install -e .  # Install package
python -m spacy download en_core_web_md # Install required spacy models
mv simplify_task1.py muss/scripts/
mv simplify_task2.py muss/scripts/