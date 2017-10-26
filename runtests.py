import os
import sys
import time
import subprocess

import django


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    if hasattr(django, 'setup'):  # Only compatible with Django >= 1.7
        django.setup()

    # For Django 1.6, need to import after setting DJANGO_SETTINGS_MODULE.
    from django.conf import settings
    from django.test.utils import get_runner

    node = subprocess.Popen(['node', 'render.js'])
    # Wait for service to start
    time.sleep(1)

    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['tests'])

    node.kill()

    sys.exit(bool(failures))
