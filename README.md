# My MCP Project

基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) 的自定义工具服务，供 AI 助手通过 MCP 调用各种操作能力。

## 功能

### 当前可用工具

- **按用户名查邮箱**：根据用户名返回对应邮箱地址（格式：`{username}@shopee.com`）
- **发送邮件**：向指定收件人发送邮件正文（模拟实现）

### 扩展能力

项目支持轻松扩展更多工具，只需在 `tools/` 目录下添加新的工具模块并在 `main_mcp.py` 中注册即可。

## 环境要求

- Python 3.8+
- 依赖见 `requirements.txt`

## 安装

1. 克隆项目
```bash
git clone <repository-url>
cd my_mcp
```

2. 创建虚拟环境（推荐）
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或 .venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 配置环境变量（可选）
```bash
cp .env.example .env
# 编辑 .env 文件设置必要的配置
```

## 运行

### 1. 启动 MCP 服务

以 stdio 方式启动 MCP 服务（供 Cursor 等客户端连接）：

```bash
python main_mcp.py
```

### 2. 运行代理客户端示例

使用代理客户端与 MCP 服务交互（需要配置 API 密钥）：

```bash
python main_agent.py
```

## 项目结构

```
my_mcp/
├── main_mcp.py          # MCP 服务入口，注册工具
├── main_agent.py        # 代理客户端示例，与外部 API 交互
├── tools/
│   └── email_operations.py   # 邮箱操作工具实现
├── .env                 # 环境变量配置文件
├── .gitignore
├── requirements.txt     # Python 依赖
└── README.md
```

## MCP 工具说明

| 工具名称 | 功能描述 | 参数 | 返回值 |
|----------|----------|------|--------|
| `get_email_address_by_username` | 根据用户名返回邮箱地址 | `username: str` | 邮箱地址字符串 |
| `send_email` | 向指定邮箱发送邮件 | `recipient_email: str`, `body: str` | 发送状态和消息 |

### 在 MCP 客户端中使用

在支持 MCP 的客户端（如 Cursor）中配置本 MCP 服务器后，即可在对话中让 AI 助手调用这些工具。

## 代理客户端说明

`main_agent.py` 是一个代理客户端示例，演示了如何：
1. 接收用户输入
2. 调用外部 AI API 生成响应
3. 处理模型的工具调用请求
4. 执行相应的工具函数
5. 将工具执行结果返回给模型
6. 获取最终的模型响应

**注意**：使用代理客户端需要配置相应的 API 密钥。

## 开发指南

### 添加新工具

1. 在 `tools/` 目录下创建新的 Python 模块
2. 实现工具函数，确保有清晰的文档字符串
3. 在 `main_mcp.py` 中导入并注册工具

示例：
```python
# tools/new_tool.py
def my_new_tool(param: str) -> str:
    """工具描述"""
    return f"处理结果: {param}"

# main_mcp.py
from tools import new_tool
mcp.add_tool(new_tool.my_new_tool)
```

## 故障排除

- **MCP 连接问题**：确保 MCP 服务正在运行，且客户端配置正确
- **依赖安装失败**：检查 Python 版本和网络连接
- **工具调用失败**：检查工具函数的参数和返回值格式

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。