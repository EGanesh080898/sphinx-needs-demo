Dashboards
==========

Open Work
---------

.. needtable:: Open Needs by Component
   :columns: id;type;status;title;component;owner;links
   :filter: status in ["open", "in_progress"]
   :sort: component

Gaps & Traceability
-------------------

.. needtable:: Requirements Missing Specs
   :columns: id;title;component
   :filter: type == "req" and len(backward_links(type=='spec')) == 0

.. needtable:: Requirements Missing Tests
   :columns: id;title;component
   :filter: type == "req" and len(backward_links(type=='test')) == 0

.. needtable:: Requirements Missing Implementations
   :columns: id;title;component
   :filter: type == "req" and len(backward_links(type=='impl')) == 0
