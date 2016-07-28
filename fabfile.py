# encoding: utf-8
from fabric import colors
from fabric.api import hosts, env, local, run, cd, puts, prefix, sudo

REMOTE_WORKDIR = '/home/ubuntu/VirtualEnvs/djangoServerVirtual/attoHome'
SERVERS = ['attocu.be','52.78.90.137']
VIRTUALENV_DIR = '/home/ubuntu/VirtualEnvs/djangoServerVirtual'
REMOTE_REQDIR = REMOTE_WORKDIR + '/install'
ACTIVATE = 'source %s/bin/activate' % VIRTUALENV_DIR

env.roledefs = {
    'app': ['ubuntu@attocu.be:22'],
}

@hosts(['attocu.be'])
def deploy():
    env.user = 'ubuntu'
    env.password = 'dkxhcube!@'

    with cd(REMOTE_WORKDIR):
        puts(colors.blue("%s:%s -> 프로젝트를 업데이트 합니다.") % (env.host, env.port))
        if env.host in SERVERS:
            run('git pull origin master')
            puts(colors.blue("프론트엔드 의존성 패키지를 업데이트합니다."))
        else:
            puts('Deploy 대상이 잘못 되었습니다. [Deploy 가능 대상 : app]')
        with prefix(ACTIVATE):
            puts(colors.blue("Reqirements를 자동으로 설치합니다."))
            run('pip install -r install/requirement.txt')
            run('python manage.py collectstatic --noinput')
            sudo('supervisorctl restart all', quiet=True)
