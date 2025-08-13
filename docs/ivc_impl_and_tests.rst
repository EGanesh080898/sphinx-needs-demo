Implementation & Tests
======================

.. impl:: Beacon sender implementation
   :id: IMPL_IVC_001
   :status: in_progress
   :links: SPEC_IVC_001, SPEC_IVC_002, REQ_IVC_001
   :component: transport

   Implements multicast beacon transmission loop with jitter and backoff.

.. impl:: Health monitor implementation
   :id: IMPL_IVC_002
   :status: open
   :links: SPEC_IVC_003, REQ_IVC_004
   :component: health

   Periodically evaluates peer liveness and emits events to control plane.

.. test:: Multicast beacon emission test
   :id: TEST_IVC_001
   :status: open
   :links: REQ_IVC_001, SPEC_IVC_001, IMPL_IVC_001
   :component: transport

   Verifies beacon sent on the configured multicast group at correct intervals.

.. test:: Loss detection timeout test
   :id: TEST_IVC_002
   :status: open
   :links: REQ_IVC_004, SPEC_IVC_003, IMPL_IVC_002
   :component: health

   Ensures peer is marked unreachable within 3000 ms after missed beacons.

Coverage — Requirements without Tests
-------------------------------------

.. needtable:: Untested Requirements
   :columns: id;title;component
   :filter: type == "req" and len(backward_links(type=='test')) == 0

Coverage — Requirements without Implementations
-----------------------------------------------

.. needtable:: Unimplemented Requirements
   :columns: id;title;component
   :filter: type == "req" and len(backward_links(type=='impl')) == 0
