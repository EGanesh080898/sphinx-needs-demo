Process
=======

A tiny example of using a custom *process* type to document the flow.

.. process:: Plan
   :id: PROC_IVC_001
   :status: done
   :owner: pm

   Define scope and success metrics.

.. process:: Design
   :id: PROC_IVC_002
   :status: in_progress
   :owner: architect
   :links: PROC_IVC_001

   Draft protocol spec and transport architecture.

.. process:: Implement
   :id: PROC_IVC_003
   :status: open
   :owner: dev-team
   :links: PROC_IVC_002

   Implement sender/receiver and health monitor.

.. process:: Test
   :id: PROC_IVC_004
   :status: open
   :owner: qa
   :links: PROC_IVC_003

   Unit, integration, soak tests in a lab network.

.. needlist:: Process Steps
   :filter: type == "process"
   :sort: id
