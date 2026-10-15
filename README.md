# jqxx — DVC 数据版本控制项目

基于 **Data Version Control (DVC)** + **Git** 对外贸指数数据集 `raw_dataset.csv` 进行版本管理与数据分析。

## 项目结构

```
.
├── data/
│   ├── raw_dataset.csv          # 真实数据集（23.3MB，由 DVC 管理，不入 Git）
│   ├── raw_dataset.csv.dvc      # DVC 指针（记录数据哈希）
│   ├── dvc_demo.csv             # 演示数据集（当前 = v2）
│   └── dvc_demo.csv.dvc         # 演示数据指针
├── analyze_data.py              # Python 数据分析脚本
├── .dvc/config                  # DVC 远程配置（myazure / local）
└── .gitignore
```

## 数据集说明

- **规模**：104,613 行 × 13 列
- **内容**：新西兰外贸指数（Overseas Trade Indexes）
  - 贸易量指数 OTV（66,347 条）
  - 贸易价格指数 OTP（37,365 条）
- **时间范围**：1925.06 ～ 2024.06
- **单位**：Index（76,336）、Dollars（24,908）、Percent（1,879）

## 数据分析（analyze_data.py）

```bash
python analyze_data.py
```

输出数据概览、缺失值、描述性统计、分类分布与时间范围等。

## DVC 数据版本控制

```bash
dvc status          # 查看跟踪状态
dvc push            # 上传数据到远程
dvc pull            # 拉取数据
git tag             # 版本标签：dvc-demo-v1 / dvc-demo-v2
git switch <tag> && dvc pull   # 切换到指定版本数据
```

> 说明：Git 仓库只存 `.dvc` 指针文件，真实数据存放在 DVC 远程存储（本地目录或 Azure Blob）。克隆本仓库后需 `dvc pull` 才能取回数据。

## 版本演示

- `dvc-demo-v1`：2 条记录
- `dvc-demo-v2`：3 条记录
