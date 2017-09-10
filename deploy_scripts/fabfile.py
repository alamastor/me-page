from fabric.api import env, run, local
from fabric.contrib.files import exists

REPO_URL = 'git@github.com:alamastor/me-page.git'


def deploy():
    site_dir = f'~/sites/{env.host}'
    _setup_dirs_if_required(site_dir)
    _update_source(site_dir)


def _setup_dirs_if_required(site_dir):
    if not exists(site_dir):
        run(f'mkdir -p {site_dir}')


def _update_source(site_dir):
    if exists(f'{site_dir}/.git'):
        run(f'cd {site_dir} && git fetch')
    else:
        run(f'git clone {REPO_URL} {site_dir}')
    current_commit = local('git log -n 1 --format=%H', capture=True)
    run(f'cd {site_dir} && git reset --hard {current_commit}')

