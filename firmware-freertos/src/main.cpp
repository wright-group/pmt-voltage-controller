#include "FreeRTOS.h"
#include "task.h"

void vTask2(void *pvParameters)
{
  printf("[TASK 2] BEGIN\n");
  for (;;)
  {
    vTaskDelay(1000);
    printf("[TASK 2] %lu\n", xTaskGetTickCount());
  }
}

void vTask1(void *pvParameters)
{
  printf("[TASK 1] BEGIN\n");
  gpio_init(PICO_DEFAULT_LED_PIN);
  gpio_set_dir(PICO_DEFAULT_LED_PIN, GPIO_OUT);
  for (;;)
  {
    gpio_put(PICO_DEFAULT_LED_PIN, 1);
    vTaskDelay(1000);
    gpio_put(PICO_DEFAULT_LED_PIN, 0);
    vTaskDelay(1000);
    printf("[TASK 1] %lu\n", to_ms_since_boot(get_absolute_time()));
  }
}

int main(void)
{
  stdio_init_all();
  printf("\n\nFreeRTOS Raspberrypi PI Pico 2021 Georgi Angelov\n");

  xTaskCreate(
      vTask1,               /* Function that implements the task. */
      "vTask1",             /* Text name for the task. */
      512,                  /* Stack size in words, not bytes. */
      (void *)1,            /* Parameter passed into the task. */
      tskIDLE_PRIORITY + 2, /* Priority at which the task is created. */
      NULL);

  xTaskCreate(
      vTask2,               /* Function that implements the task. */
      "vTask2",             /* Text name for the task. */
      512,                  /* Stack size in words, not bytes. */
      (void *)2,            /* Parameter passed into the task. */
      tskIDLE_PRIORITY + 2, /* Priority at which the task is created. */
      NULL);

  vTaskStartScheduler();
}
