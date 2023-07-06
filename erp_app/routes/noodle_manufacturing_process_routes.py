```python
from flask import Blueprint, request, redirect, url_for, flash
from erp_app.models.noodle_manufacturing_process import NoodleManufacturingProcess
from erp_app.services.noodle_manufacturing_process_service import start_process, end_process

noodle_manufacturing_process_bp = Blueprint('noodle_manufacturing_process_bp', __name__)

@noodle_manufacturing_process_bp.route('/start_process', methods=['POST'])
def start_noodle_process():
    form_data = request.form
    process = NoodleManufacturingProcess(form_data)
    if start_process(process):
        flash('process_start')
        return redirect(url_for('dashboard.html'))
    else:
        flash('process_failure')
        return redirect(url_for('noodle_manufacturing_process.html'))

@noodle_manufacturing_process_bp.route('/end_process', methods=['POST'])
def end_noodle_process():
    form_data = request.form
    process = NoodleManufacturingProcess(form_data)
    if end_process(process):
        flash('process_end')
        return redirect(url_for('dashboard.html'))
    else:
        flash('process_failure')
        return redirect(url_for('noodle_manufacturing_process.html'))
```