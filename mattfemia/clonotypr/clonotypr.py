from flask import Flask, Blueprint, url_for, render_template, redirect, request, flash

clonotypr = Blueprint(name='clonotypr',
                    import_name=__name__,
                    static_folder='clonotypr/static',
                    static_url_path=None,
                    template_folder='templates',
                    url_prefix='clonotypr',
                    subdomain=None,
                    url_defaults=None,
                    root_path=None)

@clonotypr.route('/', methods=['GET'])
def index():
    return render_template('clonotypr/index.html')

@clonotypr.route('/authors', methods=['GET'])
def authors():
    return render_template('clonotypr/authors.html')

@clonotypr.route('/404', methods=['GET'])
def not_found():
    return render_template('clonotypr/404.html')

@clonotypr.route('/license', methods=['GET'])
def license():
    return render_template('clonotypr/LICENSE-text.html')

@clonotypr.route('/changelog', methods=['GET'])
def changelog():
    return render_template('clonotypr/news/index.html')

@clonotypr.route('/articles/', methods=['GET'])
def articles():
    return render_template('clonotypr/articles/articles.html')

@clonotypr.route('/articles/vignette', methods=['GET'])
def vignette():
    return render_template('clonotypr/articles/clonotypr.html')

@clonotypr.route('/reference/', methods=['GET'])
def reference():
    return render_template(f'clonotypr/reference/reference.html')

@clonotypr.route('/reference/<function>', methods=['GET'])
def function_doc(function):
    function = function
    return render_template(f'clonotypr/reference/{function}')