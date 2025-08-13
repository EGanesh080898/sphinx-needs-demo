Requirements
============

.. req:: Multicast address and port shall be configurable
   :id: REQ_IVC_003
   :status: open
   :tags: networking
   :priority: medium
   :component: transport
   :owner: ganesh

   The multicast address and UDP port shall be configurable via a runtime config file.

.. req:: Beacon loss detection within 3000 ms
   :id: REQ_IVC_004
   :status: open
   :tags: reliability
   :priority: high
   :component: health
   :owner: team-ivc

   A peer shall be considered unreachable if **N** consecutive beacons are missed resulting in a detection within 3000 ms.

.. needtable:: All Requirements
   :columns: id;status;title;tags;component;links
   :filter: type == "req"
   :sort: id
