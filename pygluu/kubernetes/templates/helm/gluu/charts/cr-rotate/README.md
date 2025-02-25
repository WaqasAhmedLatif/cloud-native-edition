# cr-rotate

![Version: 1.6.11](https://img.shields.io/badge/Version-1.6.11-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 4.3.0](https://img.shields.io/badge/AppVersion-4.3.0-informational?style=flat-square)

CacheRefreshRotation is a special container to monitor cache refresh on oxTrust containers. This may become depreciated in 5.0.

**Homepage:** <https://gluu.org/docs/gluu-server>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Mohammad Abudayyeh | support@gluu.org | https://github.com/moabu |

## Source Code

* <https://gluu.org/docs/gluu-server/>
* <https://github.com/GluuFederation/docker-cr-rotate>
* <https://github.com/GluuFederation/cloud-native-edition/tree/4.3/pygluu/kubernetes/templates/helm/gluu/charts/cr-rotate>

## Requirements

Kubernetes: `>=v1.18.0-0`

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| additionalAnnotations | object | `{}` | Additional annotations that will be added across all resources  in the format of {cert-manager.io/issuer: "letsencrypt-prod"}. key app is taken |
| additionalLabels | object | `{}` | Additional labels that will be added across all resources definitions in the format of {mylabel: "myapp"} |
| dnsConfig | object | `{}` | Add custom dns config |
| dnsPolicy | string | `""` | Add custom dns policy |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` | Image pullPolicy to use for deploying. |
| image.pullSecrets | list | `[]` | Image Pull Secrets |
| image.repository | string | `"gluufederation/cr-rotate"` | Image  to use for deploying. |
| image.tag | string | `"4.3.0_01"` | Image  tag to use for deploying. |
| nameOverride | string | `""` |  |
| resources | object | `{"limits":{"cpu":"200m","memory":"200Mi"},"requests":{"cpu":"200m","memory":"200Mi"}}` | Resource specs. |
| resources.limits.cpu | string | `"200m"` | CPU limit. |
| resources.limits.memory | string | `"200Mi"` | Memory limit. |
| resources.requests.cpu | string | `"200m"` | CPU request. |
| resources.requests.memory | string | `"200Mi"` | Memory request. |
| service.crRotateServiceName | string | `"cr-rotate"` | Name of the cr-rotate service. Please keep it as default. |
| service.name | string | `"http-cr-rotate"` | The name of the cr-rotate port within the cr-rotate service. Please keep it as default. |
| service.port | int | `8084` | Port of the casa service. Please keep it as default. |
| usrEnvs.normal | object | `{}` | Add custom normal envs to the service variable1: value1 |
| usrEnvs.secret | object | `{}` | Add custom secret envs to the service variable1: value1 |
| volumeMounts | list | `[]` | Configure any additional volumesMounts that need to be attached to the containers |
| volumes | list | `[]` | Configure any additional volumes that need to be attached to the pod |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.5.0](https://github.com/norwoodj/helm-docs/releases/v1.5.0)
