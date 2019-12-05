# ClusterBuilder for vSphere   

This project is an adaptation of Heptio Wardroom which deployes Kubernetes components on pre-existing infrastructure via the kubeadm project.

To use this tool follow these steps:

### Prerequisites

-   Ansible pre-installed on a workstation
-   Previously deployed virtual machines which will act as kubernetes nodes

### Update Variables

Before running this playbook, update [inventory/group_vars/{environment_name}/all](inventory/group_vars/{environment_name}/all) with the environment variables specific to your vSphere and Kubernetes clusters. These settings include locations of Kubernetes nodes in vsphere as well as api and kubelet configuration options for your deployment.

Next, update the [inventory/{environment_name}.ini](inventory/{environment_name}.ini) file with the ip or dns information for your nodes.

Once the configurations have been created, build your cluster with the command:

```bash
ansible-playbook playbooks/build_cluster.yml -i inventory/{environment_name}.ini
```


