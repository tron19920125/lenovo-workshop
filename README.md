# Azure 资源清单

## 1. 核心基础设施资源

| 资源类型                     | 用途           | 配置要求             | 官方文档链接                                                                                                    |
| ------------------------ | ------------ | ---------------- | --------------------------------------------------------------------------------------------------------- |
| **Azure订阅**              | 所有资源的计费和管理   | 有效的付费订阅          | [Azure订阅管理](https://docs.microsoft.com/azure/cost-management-billing/manage/subscription-disabled)        |
| **资源组**                  | 逻辑容器，组织相关资源  | 选择合适的区域          | [资源组管理](https://docs.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal) |
| **Azure ML工作区**          | 机器学习项目核心工作空间 | 支持在线端点和计算实例      | [Azure ML工作区](https://docs.microsoft.com/azure/machine-learning/concept-workspace)                        |
| **存储账户**                 | 存储模型、数据集、日志  | 公网访问、密钥访问、Blob存储 | [Azure存储定价](https://azure.microsoft.com/pricing/details/storage/blobs/)                                   |
| **Key Vault**            | 存储敏感信息       | 标准层              | [Key Vault定价](https://azure.microsoft.com/pricing/details/key-vault/)                                     |
| **Application Insights** | 监控和日志        | 标准配置             | [Application Insights定价](https://azure.microsoft.com/pricing/details/monitor/)                            |
| **Log Analytics**        | 日志收集分析       | 与App Insights集成  | [Log Analytics定价](https://azure.microsoft.com/pricing/details/monitor/)                                   |

## 2. 容器和注册表资源

| 资源类型                 | 用途         | 配置要求          | 官方文档链接                                                                   |
| -------------------- | ---------- | ------------- | ------------------------------------------------------------------------ |
| **Azure容器注册表 (ACR)** | 存储Docker镜像 | 基本SKU，启用管理员用户 | [ACR定价](https://azure.microsoft.com/pricing/details/container-registry/) |

## 3. 计算资源

| 资源类型        | 用途        | 配置要求                     | 官方文档链接                                                                        |
| ----------- | --------- | ------------------------ | ----------------------------------------------------------------------------- |
| **AKS集群**   | 运行ML扩展和推理 | 最少4vCPU+14GB内存           | [AKS定价](https://azure.microsoft.com/pricing/details/kubernetes-service/)      |
| **GPU计算实例** | 大模型推理     | Standard_NC24ads_A100_v4 | [Azure ML计算定价](https://azure.microsoft.com/pricing/details/machine-learning/) |
| **虚拟网络**    | AKS网络支持   | 标准配置                     | [虚拟网络定价](https://azure.microsoft.com/pricing/details/virtual-network/)        |
| **负载均衡器**   | 推理流量分发    | 标准SKU                    | [负载均衡器定价](https://azure.microsoft.com/pricing/details/load-balancer/)         |

## 4. AI和机器学习服务

| 资源类型                       | 用途          | 配置要求       | 官方文档链接                                                                                           |
| -------------------------- | ----------- | ---------- | ------------------------------------------------------------------------------------------------ |
| **Azure OpenAI** (可选)      | OpenAI模型API | GPT-4等模型访问 | [Azure OpenAI定价](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) |
| **Hugging Face Hub Token** | 访问HF模型库     | 有效的API密钥   | [Hugging Face定价](https://huggingface.co/pricing)                                                 |

## 5. 网络和安全资源

| 资源类型            | 用途      | 配置要求      | 官方文档链接                                                                                                  |
| --------------- | ------- | --------- | ------------------------------------------------------------------------------------------------------- |
| **网络安全组 (NSG)** | 控制网络访问  | AKS集群安全规则 | [NSG文档](https://docs.microsoft.com/azure/virtual-network/network-security-groups-overview)              |
| **托管标识**        | 无密码身份验证 | 系统分配或用户分配 | [托管标识文档](https://docs.microsoft.com/azure/active-directory/managed-identities-azure-resources/overview) |

## 6. 必需的Azure权限和角色

| 角色名称 | 用途 | 分配范围 | 文档链接 |
|---------|------|----------|----------|
| **存储 Blob 数据参与者** | 模型和数据访问 | 存储账户 | [RBAC角色](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) |
| **AcrPull** | 容器镜像拉取 | 容器注册表 | [ACR角色](https://docs.microsoft.com/azure/container-registry/container-registry-roles) |
| **Azure ML工作区参与者** | 管理ML资源 | ML工作区 | [ML角色](https://docs.microsoft.com/azure/machine-learning/how-to-assign-roles) |
| **Kubernetes服务参与者** | 管理AKS资源 | AKS集群 | [AKS RBAC](https://docs.microsoft.com/azure/aks/manage-azure-rbac) |

## 7. 必需的服务注册

| 服务提供程序 | 用途 | 注册命令 | 文档链接 |
|-------------|------|----------|----------|
| **KubernetesConfiguration** | AKS扩展支持 | `az provider register --namespace Microsoft.KubernetesConfiguration` | [服务提供程序注册](https://docs.microsoft.com/azure/azure-resource-manager/management/resource-providers-and-types) |
| **MachineLearningServices** | Azure ML服务 | `az provider register --namespace Microsoft.MachineLearningServices` | [ML服务注册](https://docs.microsoft.com/azure/machine-learning/how-to-manage-workspace) |

## 相关重要链接

| 类别 | 链接 | 说明 |
|------|------|------|
| **Azure ML文档** | [Azure ML官方文档](https://docs.microsoft.com/azure/machine-learning/) | 完整的Azure ML服务文档 |
| **成本管理** | [Azure成本计算器](https://azure.microsoft.com/pricing/calculator/) | 精确估算成本 |
| **最佳实践** | [ML安全最佳实践](https://docs.microsoft.com/azure/machine-learning/concept-enterprise-security) | 企业级安全配置 |
| **故障排除** | [Azure ML故障排除](https://docs.microsoft.com/azure/machine-learning/how-to-troubleshoot-deployment) | 常见问题解决方案 |
