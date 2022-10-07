<template>
  <q-header elevated dark class="bg-transparent">
      <q-toolbar class="row bg-transparent q-my-sm" dark>
        <div class="col-2" style="max-width:200px"></div>
        <div class="row col q-mr-md">
				<q-icon
				 name="hub"
				 round
				 size="sm"
				 class="graph-button"
				 @click="openGraph"
				/>


            <q-toolbar-title class="content-center flex">
            Mafia-SDG Docs
            </q-toolbar-title>


        </div>
            <q-select class="col q-mx-lg" dense rounded  outlined v-model="searchSelection" @input-value="search" use-input input-debounce="0" label="Search docs..." :options="searchResults || []" behaviour="menu" >
                <template v-slot:no-option >
                    <q-item>
                        <q-item-section class="text-grey">
                        No results
                        </q-item-section>
                    </q-item>
                </template>
                <template v-slot:option="scope">
                    <q-item class='' v-bind="scope.itemProps" style="max-height: 200px" clickable @click="openNote(scope.opt)">
                        <q-item-section avatar class="" style="width:100px">
                            <q-item-label>{{ scope.opt.label }}</q-item-label>
                        </q-item-section>
						<q-separator vertical inset spaced />
                        <q-item-section>
                            <q-scroll-area class="fit">
                                <q-markdown :src="scope.opt.value"  no-heading-anchor-links :plugins="plugins" />
                            </q-scroll-area>

                        </q-item-section >
                    </q-item>
					<q-separator inset />
                </template>
            </q-select>
        <div class="">
			<q-btn rounded flat class="text-italic text-accent text-bold" no-caps>
				<div>
					Scuffed  <q-badge color="secondary bg-transparent" transparent dense floating >v{{ version }}</q-badge>
				</div>
			</q-btn>
            <!-- <span class="text-accent text-italic text-bold">Scuffed</span> -->
        </div>
		<div class="coln" style="max-width: 200px">

		</div>
      </q-toolbar>
    </q-header>
</template>

<script>
import { fuse } from 'src/boot/fuse'
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import contentItems from '../content/.map.json'
import { version } from '../../package.json'
import taskLists from 'markdown-it-task-lists'
import admonition from 'markdown-it-admonition'

export default {
  name: 'SToolbar',
  setup () {
		const router = useRouter()

        const openGraph = () => {
            // TODO
            console.log('opening graph')
			router.push('/graph')
        }

        const searchTerms = ref('')

        const search = (val) => {
            searchTerms.value = val
        }

        const searchResults = computed(() => {
            console.log(fuse.search(searchTerms.value), searchTerms.value)
            return (fuse.search(searchTerms.value).map(
                (result) => {
                    // console.log({label: result.item.title, value: result.item.body, src: result.item.src})
					let output = []
					// console.log('search result', result.item.body.split('\n'))
					const lines = result.item.body.split('\n')
					for (let [index, line] of Object.entries(lines)) {
						if (line.indexOf(searchTerms.value) > -1) {
							if (index > 3) output.push(lines[index-4])
							output.push(line)
							if (index < lines.length - 3) output.push(lines[index+4])
							break
						}
					}

					// return null
					console.log('output', output)
					if (output.length) {
						return { label: result.item.title.split('.')[0], value: output.join('\n'), src: result.item.src }
					} else {
						return null
					}
                }
            )).filter(i => {
				console.log('i', i)
				return i !== null
			})
        })

        const searchSelection = ref(null)


		const openNote = (note) => {
			// console.log('note', note)
			searchSelection.value = null
			router.push(note.src.replace('#', ''))
		}

        return {
			contentItems,
			openGraph,
			searchTerms,
			search,
			searchResults,
			searchSelection,
			openNote,
			version: version,
			plugins: [
				taskLists,
				{plugin: admonition, options: {marker: '!', types: ["note", "abstract", "info", "tip", "success", "question", "warning", "failure", "danger", "bug", "example", "quote", "night-actions", "day-actions", "special-actions"]}}
			]
        }
    }
}
</script>

<style scoped >

.graph-button {
	color: #00FFFF;
	-webkit-transition: color 200ms linear;
    -ms-transition: color 200ms linear;
    transition: color 200ms linear;
}

.graph-button:hover{
	color: hotpink; /* TODO */
	cursor: pointer;

}

</style>
