import { useQMarkdownGlobalProps } from '@quasar/quasar-ui-qmarkdown'
import taskLists from 'markdown-it-task-lists'

// defaults for QMarkdown
useQMarkdownGlobalProps({
  plugins: [taskLists]
})
