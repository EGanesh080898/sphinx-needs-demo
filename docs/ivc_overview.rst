Overview
========

The IVC module enables vehicle-to-vehicle data exchange for cooperative driving features.

Goals:
- Low-latency message delivery
- Reliable dissemination over lossy wireless links
- Support for UDP unicast and multicast

Below is a small set of needs representing a thin slice of the lifecycle.

.. req:: Support UDP multicast for neighbor discovery
   :id: REQ_IVC_001
   :status: open
   :tags: networking, reliability
   :priority: high
   :component: transport
   :owner: ganesh

   The IVC module shall support UDP multicast for periodic neighbor discovery beacons on the configured interface.

.. req:: End-to-end latency under 50 ms in same-hop links
   :id: REQ_IVC_002
   :status: open
   :tags: performance
   :priority: high
   :component: transport
   :owner: team-ivc

   For same-hop communications, the average end-to-end latency for 95% of packets must be under **50 ms**.

.. spec:: Beaconing protocol specification
   :id: SPEC_IVC_001
   :status: in_progress
   :links: REQ_IVC_001, REQ_IVC_002
   :component: transport

   Defines packet format, multicast address/port, send interval, jitter, and congestion backoff rules.
