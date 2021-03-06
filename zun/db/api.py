# Copyright 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""
Base API for Database
"""

import abc

from oslo_config import cfg
from oslo_db import api as db_api
import six

"""Add the database backend mapping here"""

_BACKEND_MAPPING = {'sqlalchemy': 'zun.db.sqlalchemy.api'}
IMPL = db_api.DBAPI.from_config(cfg.CONF, backend_mapping=_BACKEND_MAPPING,
                                lazy=True)


def get_instance():
    """Return a DB API instance."""
    """Add more judgement for selecting more database backend"""
    return IMPL


@six.add_metaclass(abc.ABCMeta)
class Connection(object):
    """Base class for storage system connections."""

    def __init__(self):
        """Constructor."""
        pass

    @classmethod
    def list_container(cls, context, filters=None,
                       limit=None, marker=None,
                       sort_key=None, sort_dir=None):
        """Get matching containers.

        Return a list of the specified columns for all containers that match
        the specified filters.
        :param context: The security context
        :param filters: Filters to apply. Defaults to None.
        :param limit: Maximum number of containers to return.
        :param marker: the last item of the previous page; we return the next
                       result set.
        :param sort_key: Attribute by which results should be sorted.
                         (asc, desc)
        :returns: A list of tuples of the specified columns.
        """
        dbdriver = get_instance()
        return dbdriver.list_container(
            context, filters, limit, marker, sort_key, sort_dir)

    @classmethod
    def create_container(cls, values):
        """Create a new container.

        :param values: A dict containing several items used to identify
                       and track the container, and several dicts which are
                       passed
                       into the Drivers when managing this container. For
                       example:
                       ::
                        {
                         'uuid': uuidutils.generate_uuid(),
                         'name': 'example',
                         'type': 'virt'
                        }
        :returns: A container.
        """
        dbdriver = get_instance()
        return dbdriver.create_container(values)

    @classmethod
    def get_container_by_id(self, context, container_id):
        """Return a container.

        :param context: The security context
        :param container_uuid: The uuid of a container.
        :returns: A container.
        """
        dbdriver = get_instance()
        return dbdriver.get_container_by_id(context, container_id)

    @classmethod
    def get_container_by_uuid(self, context, container_uuid):
        """Return a container.

        :param context: The security context
        :param container_uuid: The uuid of a container.
        :returns: A container.
        """
        dbdriver = get_instance()
        return dbdriver.get_container_by_uuid(context, container_uuid)

    @classmethod
    def get_container_by_name(self, context, container_name):
        """Return a container.

        :param context: The security context
        :param container_name: The name of a container.
        :returns: A container.
        """
        dbdriver = get_instance()
        return dbdriver.get_container_by_name(context, container_name)

    @classmethod
    def destroy_container(self, container_id):
        """Destroy a container and all associated interfaces.

        :param container_id: The id or uuid of a container.
        """
        dbdriver = get_instance()
        return dbdriver.destroy_container(container_id)

    @classmethod
    def update_container(self, container_id, values):
        """Update properties of a container.

        :param container_id: The id or uuid of a container.
        :returns: A container.
        :raises: ContainerNotFound
        """
        dbdriver = get_instance()
        return dbdriver.update_container(container_id, values)

    @classmethod
    def destroy_zun_service(self, zun_service_id):
        """Destroys a zun_service record.

        :param zun_service_id: The id of a zun_service.
        """
        dbdriver = get_instance()
        return dbdriver.destroy_zun_service(zun_service_id)

    @classmethod
    def update_zun_service(self, zun_service_id, values):
        """Update properties of a zun_service.

        :param zun_service_id: The id of a zun_service record.
        """
        dbdriver = get_instance()
        return dbdriver.update_zun_service(zun_service_id, values)

    @classmethod
    def get_zun_service_by_host_and_binary(cls, context, host, binary):
        """Return a zun_service record.

        :param context: The security context
        :param host: The host where the binary is located.
        :param binary: The name of the binary.
        :returns: A zun_service record.
        """
        dbdriver = get_instance()
        return dbdriver.get_zun_service_by_host_and_binary(
            context, host, binary)

    @classmethod
    def create_zun_service(self, values):
        """Create a new zun_service record.

        :param values: A dict containing several items used to identify
                       and define the zun_service record.
        :returns: A zun_service record.
        """
        dbdriver = get_instance()
        return dbdriver.create_zun_service(values)

    @classmethod
    def get_zun_service_list(cls, context, disabled=None, limit=None,
                             marker=None, sort_key=None, sort_dir=None):
        """Get matching zun_service records.

        Return a list of the specified columns for all zun_services
        those match the specified filters.

        :param context: The security context
        :param disabled: Filters disbaled services. Defaults to None.
        :param limit: Maximum number of zun_services to return.
        :param marker: the last item of the previous page; we return the next
                       result set.
        :param sort_key: Attribute by which results should be sorted.
        :param sort_dir: direction in which results should be sorted.
                         (asc, desc)
        :returns: A list of tuples of the specified columns.
        """
        dbdriver = get_instance()
        return dbdriver.get_zun_service_list(
            context, disabled, limit, marker, sort_key, sort_dir)
