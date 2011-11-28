
Woven
=====

Woven deploys versioned Django projects onto Linux servers behind
Nginx using Apache modwsgi by default. Woven is is built on
`Fabric <http://docs.fabfile.org/>`_.

.. Note::

   Woven is still alpha software, and the API and conventions may
   change between versions. It is *not* recommended for production
   deployment at this stage.

   Woven has been tested using `Ubuntu Server
   <http://www.ubuntu.com/business/server/overview>` 10.04 and
   greater. It may work on other Debian-based distributions, but needs
   some work to be compatible with other Linux distros.

   It currently *won't* work at all with Windows, due to use of rsync,
