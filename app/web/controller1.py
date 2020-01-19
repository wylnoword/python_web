from . import bp


@bp.route('/view2')
def view2():
    return '这是视图2'
