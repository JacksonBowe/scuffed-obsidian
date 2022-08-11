import { useQMarkdownGlobalProps } from '@quasar/quasar-ui-qmarkdown'
import taskLists from 'markdown-it-task-lists'

console.log('fuck this')

// defaults for QMarkdown
useQMarkdownGlobalProps({
  plugins: [taskLists]
})
