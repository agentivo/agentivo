# agentivo

Community-maintained, AI-moderated projects.

## Architecture

```
User Submission          Discovery (scheduled)
     │                         │
     │  ┌──────────────────────┘
     ▼  ▼
┌─────────────┐
│   Issues    │◄──── Community Reports
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ AI Validate │  URL check, duplicate detection, content extraction
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Auto PR    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Human Review│  Maintainer approves/rejects
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Deploy    │
└─────────────┘
```

## Principles

- **Low barrier**: Casual submissions accepted, AI extracts structure
- **Multi-source discovery**: Automated scraping from Reddit, HN, GitHub Topics
- **Validation layers**: AI review → URL check → duplicate check → human approval
- **Self-healing**: Scheduled link checks, stale content detection
- **Community feedback**: Issue templates for reporting problems

## Projects

- [student-benefits-hub](https://github.com/agentivo/student-benefits-hub) - Student discounts directory
