Insights Ansible Runner POC
===========================

Insights Ansible Runner POC

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: Apache Software License 2.0

Build Machine Requirements
--------------------------

* Docker
* NodeJS 8.11.4+
* NPM 6.4+
* GNU Make


Deployment
----------

The following details how to deploy this application.


Local Docker
^^^^^^^^^^^^

    make all


Demo Setup
----------

#. Browse to http://localhost:8000/insights_integration/api/ for the API.

#. Start up ``ansible_worker_poller`` with the following command on the jump host:
     ``ansible_worker_poller http://localhost:8000 1 --wait_time=1``
#. Browse to the API and add entries for inventory, key, hosts, worker, and workerqueue.
#. Use the ``sync_with_insights`` management command to copy a plan and playbook into the database.


Demo
----

#. Browse to http://localhost:8000 for the main page so see the playbook and hosts.
#. Click the ``Launch Playbook`` button to run the playbook against the target inventory.
