#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke tasks."""
import os
import json
import shutil
import webbrowser

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'cookiecutter.json'), 'r') as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
COOKIE = os.path.join(HERE, COOKIECUTTER_SETTINGS['repo_name'])
REQUIREMENTS = os.path.join(COOKIE, 'dev-requirements.txt')


@task
def build(ctx):
    """Build the cookiecutter."""
    ctx.run('cookiecutter {0} --no-input'.format(HERE))


@task
def clean(ctx):
    """Clean out generated cookiecutter."""
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print('Removed {0}'.format(COOKIE))
    else:
        print('App directory does not exist. Skipping.')


@task(pre=[clean, build])
def test(ctx):
    """Run lint commands and tests."""
    ctx.run('pip install -r {0} --ignore-installed'.format(REQUIREMENTS),
            echo=True)
    os.chdir(COOKIE)
    ctx.run('python setup.py test', echo=True)


@task
def readme(ctx, browse=False):
    ctx.run("rst2html.py README.rst > README.html")
    if browse:
        webbrowser.open_new_tab('README.html')
