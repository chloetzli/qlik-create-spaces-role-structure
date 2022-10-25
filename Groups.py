from __future__ import annotations

import warnings
from dataclasses import asdict, dataclass

from qlik_sdk import Auth, Config
from qlik_sdk import ListableResource

@dataclass
class Group:
    """

    Attributes
    ----------
    id: str
      A unique identifier for the group, for example, 62716f4b39b865ece543cd45.
    tenantId: str
      The ID for the tenant, for example, xqGQ0k66vSR8f9G7J-vYtHZQkiYrCpct.
    createdAt: str
      The date and time when the group was created.
    lastUpdatedAt: str
      The date and time when the group was updated.
    name: str
      The name of the group.
    links: object
    status: str
      Current status of group.
    idpId: str
      idp of origin for example, 6346c27bf619e54bf9361fd7.
    """

    id: str = None
    tenantId: str = None
    createdAt: str = None
    lastUpdatedAt: str = None
    name: str = None
    links: object = None
    status: str = None
    ipdId: str = None


    def __init__(self_, **kvargs):
        if "id" in kvargs:
            if type(kvargs["id"]).__name__ is self_.__annotations__["id"]:
                self_.id = kvargs["id"]
            else:
                self_.id = kvargs["id"]
        if "tenantId" in kvargs:
            if type(kvargs["tenantId"]).__name__ is self_.__annotations__["tenantId"]:
                self_.tenantId = kvargs["tenantId"]
            else:
                self_.tenantId = kvargs["tenantId"]
        if "createdAt" in kvargs:
            if type(kvargs["createdAt"]).__name__ is self_.__annotations__["createdAt"]:
                self_.createdAt = kvargs["createdAt"]
            else:
                self_.createdAt = kvargs["createdAt"]
        if "lastUpdatedAt" in kvargs:
            if type(kvargs["lastUpdatedAt"]).__name__ is self_.__annotations__["lastUpdatedAt"]:
                self_.lastUpdatedAt = kvargs["lastUpdatedAt"]
            else:
                self_.lastUpdatedAt = kvargs["lastUpdatedAt"]
        if "name" in kvargs:
            if type(kvargs["name"]).__name__ is self_.__annotations__["name"]:
                self_.name = kvargs["name"]
            else:
                self_.name = kvargs["name"]
        if "links" in kvargs:
            if type(kvargs["links"]).__name__ is self_.__annotations__["links"]:
                self_.links = kvargs["links"]
            else:
                self_.links = kvargs["links"]
        if "status" in kvargs:
            if type(kvargs["status"]).__name__ is self_.__annotations__["status"]:
                self_.status = kvargs["status"]
            else:
                self_.status = kvargs["status"]
        if "ipdId" in kvargs:
            if type(kvargs["ipdId"]).__name__ is self_.__annotations__["ipdId"]:
                self_.ipdId = kvargs["ipdId"]
            else:
                self_.ipdId = kvargs["ipdId"]
       
        for k, v in kvargs.items():
            if k not in getattr(self_, "__annotations__", {}):
                self_.__setattr__(k, v)

    def delete(self) -> None:
        """
        Deletes a group.

        Parameters
        ----------
        """

        self.auth.rest(
            path="/groups/{groupId}".replace("{groupId}", self.id),
            method="DELETE",
            params={},
            data=None,
        )


@dataclass
class FilterGroups:
    """

    Attributes
    ----------
    ids: list[str]
    names: list[str]
    """

    ids: list[str] = None
    names: list[str] = None

    def __init__(self_, **kvargs):
        if "ids" in kvargs:
            if type(kvargs["ids"]).__name__ is self_.__annotations__["ids"]:
                self_.ids = kvargs["ids"]
            else:
                self_.ids = kvargs["ids"]
        if "names" in kvargs:
            if type(kvargs["names"]).__name__ is self_.__annotations__["names"]:
                self_.names = kvargs["names"]
            else:
                self_.names = kvargs["names"]
        for k, v in kvargs.items():
            if k not in getattr(self_, "__annotations__", {}):
                self_.__setattr__(k, v)


@dataclass
class GroupClass:
    """

    Attributes
    ----------
    data: list[Group]
    links: object
    meta: object
    """

    data: list[Group] = None
    links: object = None
    meta: object = None

    def __init__(self_, **kvargs):
        if "data" in kvargs:
            if type(kvargs["data"]).__name__ is self_.__annotations__["data"]:
                self_.data = kvargs["data"]
            else:
                self_.data = [Group(**e) for e in kvargs["data"]]
        if "links" in kvargs:
            if type(kvargs["links"]).__name__ is self_.__annotations__["links"]:
                self_.links = kvargs["links"]
            else:
                self_.links = kvargs["links"]
        for k, v in kvargs.items():
            if k not in getattr(self_, "__annotations__", {}):
                self_.__setattr__(k, v)


class Groups:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.auth = Auth(config)

    def get_groups(
        self,
        action: str = None,
        limit: int = 10,
        name: str = None,
        next: str = None,
        ownerId: str = None,
        prev: str = None,
        sort: str = None,
        type: str = None,
        max_items: int = 10,
    ) -> ListableResource[Group]:
        """
        Retrieves groups that the current user has access to and match the query.

        limit: int
          Maximum number of groups to return.

        name: str
          Group name to search and filter for. Case-insensitive open search with wildcards both as prefix and suffix. For example, "?name=fin" will get "finance", "Final" and "Griffin".

        next: str
          The next page cursor. Next links make use of this.

        prev: str
          The previous page cursor. Previous links make use of this.

        sort: str
          Field to sort by. Prefix with +/- to indicate asc/desc. For example, "?sort=+name" to sort ascending on Name. Supported fields are "type", "name" and "createdAt".

        Parameters
        ----------
        limit: int = 10
        name: str = None
        next: str = None
        prev: str = None
        sort: str = None
        """
        query_params = {}
        if limit is not None:
            query_params["limit"] = limit
        if name is not None:
            query_params["name"] = name
        if next is not None:
            query_params["next"] = next
        if prev is not None:
            query_params["prev"] = prev
        if sort is not None:
            query_params["sort"] = sort

        response = self.auth.rest(
            path="/groups",
            method="GET",
            params=query_params,
            data=None,
        )
        return ListableResource(
            response=response.json(),
            cls=Group,
            auth=self.auth,
            path="/groups",
            max_items=max_items,
            query_params=query_params,
        )


    def create_filters(
        self, data: FilterGroups, max_items: int = 10
    ) -> ListableResource[Group]:
        """
        Experimental
        Retrieves groups that the current user has access to with provided group IDs or names.


        Parameters
        ----------
        data: FilterGroups
        """
        warnings.warn("create_filters is experimental", UserWarning, stacklevel=2)

        try:
            data = asdict(data)
            
        except:
            data = data

        response = self.auth.rest(
            path="/groups/actions/filter",
            method="POST",
            params={},
            data=data,
        )
        return ListableResource(
            response=response.json(),
            cls=Group,
            auth=self.auth,
            path="/groups/actions/filter",
            max_items=max_items,
            query_params={},
        )

    def get(self, groupId: str) -> Group:
        """
        Retrieves a single group by ID.


        groupId: str
          The ID of the group to retrieve.

        Parameters
        ----------
        groupId: str
        """

        response = self.auth.rest(
            path="/groups/{groupId}".replace("{groupId}", groupId),
            method="GET",
            params={},
            data=None,
        )
        obj = Group(**response.json())
        obj.auth = self.auth
        return obj

