Architecture
============

.. spec:: Transport layer design
   :id: SPEC_IVC_002
   :status: in_progress
   :links: REQ_IVC_003, REQ_IVC_004
   :component: transport

   Provides socket setup, IO loops, and packet scheduling.

.. spec:: Health monitor component
   :id: SPEC_IVC_003
   :status: open
   :links: REQ_IVC_004
   :component: health

   Tracks peer liveness using missed-beacon counters and timers.

.. needtable:: Architecture Specs
   :columns: id;status;title;component;links
   :filter: type == "spec"
   :sort: id
