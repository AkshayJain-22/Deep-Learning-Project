echo [$(date)] : "START"
echo [$(date)] : "Creating env with Python-3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)] : "Activating Environment"
source activate ./env
echo [$(date)] : "Installing Dev-Requirements"
pip install -r requirements_dev.txt
echo [$(date)] : "END"