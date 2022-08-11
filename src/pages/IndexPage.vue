<template>
  <q-page class="row" dark>

	<div class="q-pa-lg col-7">
		<!-- no-heading-anchor-links -->
		<q-scroll-area class="fit" :visible="false">
			<q-markdown ref="markdown" :src="content" class="q-pl-lg" :key="content" toc :toc-start="1" no-heading-anchor-links :toc-end="6"  @data="onToc" />
		</q-scroll-area>

	</div>
	<div v-if="!$q.screen.xs || !$q.screen.sm" class="q-ml-sm q-pt-lg">
		<!-- <span class="text-bold">ON THIS PAGE</span> -->
		<!-- <div class="q-pa-none" v-for="heading in toc" :key="heading">
			<span class="q-pa-none" > {{heading.label}}</span>
		</div> -->
		<q-list dense>
			<q-item-label header class="body">ON THIS PAGE</q-item-label>
			<q-item dense v-for="section in toc" :key="section" class="toc-item" :inset-level="(section.level-1) / 4"  >
				<q-item-section >
					<span v-html="section.label"  />
				</q-item-section>

			</q-item>
		</q-list>
	</div>
  </q-page>
</template>

<script>
import { defineComponent, computed, onUpdated, onMounted, ref } from 'vue'
import { useQuasar } from 'quasar'
// import markdown from "../content/Note B.md"

import {  onBeforeRouteUpdate, useRoute } from 'vue-router'

export default defineComponent({
	name: 'IndexPage',
	setup () {

		const route = useRoute()


		onMounted(async () => {
			await loadContent()
			//   await loadToc()
		})

		onUpdated(async () => {
			await loadContent()
			//   toc.value = {}
			//   await loadToc()
		})

		const content = ref(null)

		const loadContent = async () => {
			const route = useRoute()
			console.log('updated, using '+ `..${route.path}`)
			let fileData = await import(`..${route.path}` /* @vite-ignore */)
			content.value = fileData.default
		}

		// const tocTree = ref({})
		// const loadToc = async () => {
		// 	console.log(markdown.value)
		// 	tocTree.value = await markdown.value.makeTree(toc.value)
		// 	console.log('tocTree', tocTree.value)
		// }

		const markdown = ref(null)
		const toc = ref({})
		const onToc = async (x) => {
			toc.value = x
			// console.log('markdown', markdown.value)

			// toc.value = markdown.value.makeTree(toc)
			console.log(toc.value)
		}

		const q = useQuasar()


		q.dark.set(true)

		const test = (x) => {
			console.log(x)
		}


		return {
		content,
		onToc,
		markdown,
		toc,
		test
		}
	}
})
</script>

<style scoped>

.toc-item {
	opacity: 0.85;
}

.toc-item:hover {
	/* color: red; */
}


</style>
