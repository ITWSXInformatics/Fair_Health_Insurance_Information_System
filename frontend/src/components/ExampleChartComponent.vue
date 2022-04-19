<script setup>
import { ref } from 'vue'
const option = ref(
		{
				title: {
				text: 'Monthly Average Temperature',
				subtext: 'Source: WorldClimate.com',
				},
				tooltip: {
				trigger: 'axis',
				axisPointer: {
						type: 'cross',
				},
				},
				legend: {
				data: ['Highest', 'Lowest'],
				},
				toolbox: {
				show: true,
				feature: {
						dataZoom: {
						yAxisIndex: 'none',
						},
						dataView: { readOnly: false },
						magicType: { type: ['line', 'bar'] },
						restore: {},
						saveAsImage: {},
				},
				},
				xAxis: [
				{
						type: 'category',
						boundaryGap: false,
						data: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
				},
				],
				yAxis: [
				{
						type: 'value',
						axisLabel: {
						formatter: '{value} °C',
						},
				},
				],
				series: [
				{
						name: 'Highest',
						type: 'line',
						data: [11, 11, 15, 13, 12, 13, 10, 123, 123, 123, 123, 123],
				},
				{
						name: 'Lowest',
						type: 'line',
						data: [1, -2, 2, 5, 3, 2, 0, -123, -123, -123, -123, -123],
				},
				],
		},
		);
</script>

<template>
<div>
	Here is an example of apache echarts:
	<div>
		<div class="container-xl">
			<v-chart class="chart" style="min-height: 400px; width=75vw" :option="option" />
		</div>
	</div>
</div>
<p>test</p>


<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
  <label class="form-check-label" for="defaultCheck1">
    Default checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="defaultCheck2" disabled>
  <label class="form-check-label" for="defaultCheck2">
    Disabled checkbox
  </label>
</div>


</template>
<style scoped>
</style>
