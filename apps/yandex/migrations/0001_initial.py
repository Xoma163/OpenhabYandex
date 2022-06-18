# Generated by Django 4.0.4 on 2022-06-18 21:16

import apps.yandex.consts
from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Название')),
                ('type', models.CharField(choices=[(apps.yandex.consts.CapabilityType['ON_OFF'], 'ON_OFF. Удаленное включение и выключение устройства'), (apps.yandex.consts.CapabilityType['COLOR_SETTING'], 'COLOR_SETTING. Управление цветом для светящихся элементов в устройстве'), (apps.yandex.consts.CapabilityType['MODE'], 'MODE. Переключение режимов работы устройства, например, переключение между температурными режимами работы кондиционера'), (apps.yandex.consts.CapabilityType['RANGE'], 'RANGE. Управление параметрами устройства, которые имеют диапазон'), (apps.yandex.consts.CapabilityType['TOGGLE'], 'TOGGLE. Управление параметрами устройства, которые могут находиться только в одном из двух состояний'), (apps.yandex.consts.CapabilityType['VIDEO_STREAM'], 'VIDEO_STREAM. Получение видеопотока с камеры')], max_length=100, verbose_name='Тип устройства')),
                ('parameters', models.JSONField(default=dict, editable=False, verbose_name='Параметры')),
                ('retrievable', models.BooleanField(default=True, help_text='Признак включенного оповещения об изменении состояния умения при помощи сервиса уведомлений', verbose_name='Включенное оповещение')),
                ('reportable', models.BooleanField(default=False, help_text='Доступен ли для данного умения устройства запрос состояния', verbose_name='Доступен ли запрос состояния')),
                ('value', models.JSONField(blank=True, default=dict, help_text='Изначальное значение')),
                ('color_model', models.CharField(blank=True, choices=[(apps.yandex.consts.ColorModel['RGB'], 'RGB'), (apps.yandex.consts.ColorModel['HSV'], 'HSV')], max_length=10, verbose_name='Цветовая модель')),
                ('temp_k_min', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(9000)], verbose_name='Минимальная температура света')),
                ('temp_k_max', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(9000)], verbose_name='Максимальная температура света')),
                ('mode_instance', models.CharField(blank=True, choices=[(apps.yandex.consts.ModeInstance['CLEANUP_MODE'], 'CLEANUP_MODE. Установка режима уборки'), (apps.yandex.consts.ModeInstance['DISHWASHING'], 'DISHWASHING. Установка режима мытья посуды'), (apps.yandex.consts.ModeInstance['FAN_SPEED'], 'FAN_SPEED. Установка режима работы скорости вентиляции, например, в кондиционере, вентиляторе или обогревателе'), (apps.yandex.consts.ModeInstance['HEAT'], 'HEAT. Установка режима нагрева'), (apps.yandex.consts.ModeInstance['INPUT_SOURCE'], 'INPUT_SOURCE. Установка источника сигнала'), (apps.yandex.consts.ModeInstance['PROGRAM'], 'PROGRAM. Установка какой-либо программы работы'), (apps.yandex.consts.ModeInstance['SWING'], 'SWING. Установка направления воздуха в климатической технике'), (apps.yandex.consts.ModeInstance['TEA_MODE'], 'TEA_MODE. Установка режима приготовления чая'), (apps.yandex.consts.ModeInstance['THERMOSTAT'], 'THERMOSTAT. Установка температурного режима работы климатической техники, например, в кондиционере'), (apps.yandex.consts.ModeInstance['WORK_SPEED'], 'WORK_SPEED. Установка скорости работы')], max_length=50, verbose_name='instance')),
                ('modes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[(apps.yandex.consts.Mode['AUTO'], 'AUTO. Автоматический режим'), (apps.yandex.consts.Mode['ECO'], 'ECO. Экономичный режим'), (apps.yandex.consts.Mode['TURBO'], 'TURBO. Турбо'), (apps.yandex.consts.Mode['COOL'], 'COOL. Охлаждение'), (apps.yandex.consts.Mode['DRY'], 'DRY. Режим осушения'), (apps.yandex.consts.Mode['FAN_ONLY'], 'FAN_ONLY. Вентиляция'), (apps.yandex.consts.Mode['HEAT'], 'HEAT. Обогрев'), (apps.yandex.consts.Mode['PREHEAT'], 'PREHEAT. Подогрев, [разогрев, предварительный нагрев, предварительный разогрев]'), (apps.yandex.consts.Mode['HIGH'], 'HIGH. Высокая скорость'), (apps.yandex.consts.Mode['LOW'], 'LOW. Низкая скорость'), (apps.yandex.consts.Mode['MEDIUM'], 'MEDIUM. Средняя скорость'), (apps.yandex.consts.Mode['MAX'], 'MAX. Максимальный, [максимум]'), (apps.yandex.consts.Mode['MIN'], 'MIN. Минимальный, [минимум]'), (apps.yandex.consts.Mode['FAST'], 'FAST. Быстрый'), (apps.yandex.consts.Mode['SLOW'], 'SLOW. Медленный'), (apps.yandex.consts.Mode['EXPRESS'], 'EXPRESS. Экспресс'), (apps.yandex.consts.Mode['NORMAL'], 'NORMAL. Нормальный, [обычный]'), (apps.yandex.consts.Mode['QUIET'], 'QUIET. Тихий, [ночной]'), (apps.yandex.consts.Mode['HORIZONTAL'], 'HORIZONTAL. Горизонтальный'), (apps.yandex.consts.Mode['STATIONARY'], 'STATIONARY. Неподвижный, [статичный, фиксированный]'), (apps.yandex.consts.Mode['VERTICAL'], 'VERTICAL. Вертикальный'), (apps.yandex.consts.Mode['ONE'], 'ONE. Первый'), (apps.yandex.consts.Mode['TWO'], 'TWO. Второй'), (apps.yandex.consts.Mode['THREE'], 'THREE Третий'), (apps.yandex.consts.Mode['FOUR'], 'FOUR. Четвёртый'), (apps.yandex.consts.Mode['FIVE'], 'FIVE. Пятый'), (apps.yandex.consts.Mode['SIX'], 'SIX. Шестой'), (apps.yandex.consts.Mode['SEVEN'], 'SEVEN. Седьмой'), (apps.yandex.consts.Mode['EIGHT'], 'EIGHT. Восьмой'), (apps.yandex.consts.Mode['NINE'], 'NINE. Девятый'), (apps.yandex.consts.Mode['TEN'], 'TEN. Десятый'), (apps.yandex.consts.Mode['AMERICANO'], 'AMERICANO. Американо'), (apps.yandex.consts.Mode['CAPPUCCINO'], 'CAPPUCCINO. Капучино'), (apps.yandex.consts.Mode['DOUBLE_ESPRESSO'], 'DOUBLE_ESPRESSO. Двойной эспрессо'), (apps.yandex.consts.Mode['ESPRESSO'], 'ESPRESSO. Эспрессо'), (apps.yandex.consts.Mode['LATTE'], 'LATTE. Латте'), (apps.yandex.consts.Mode['BLACK_TEA'], 'BLACK_TEA. Черный чай'), (apps.yandex.consts.Mode['FLOWER_TEA'], 'FLOWER_TEA. Цветочный чай'), (apps.yandex.consts.Mode['GREEN_TEA'], 'GREEN_TEA. Зеленый чай'), (apps.yandex.consts.Mode['HERBAL_TEA'], 'HERBAL_TEA. Травяной чай'), (apps.yandex.consts.Mode['OOLONG_TEA'], 'OOLONG_TEA. Чай улун'), (apps.yandex.consts.Mode['PUERH_TEA'], 'PUERH_TEA. Чай пуэр'), (apps.yandex.consts.Mode['RED_TEA'], 'RED_TEA. Красный чай'), (apps.yandex.consts.Mode['WHITE_TEA'], 'WHITE_TEA. Белый чай'), (apps.yandex.consts.Mode['GLASS'], 'GLASS. Мойка стекла'), (apps.yandex.consts.Mode['INTENSIVE'], 'INTENSIVE. Интенсивный'), (apps.yandex.consts.Mode['PRE_RINSE'], 'PRE_RINSE. Ополаскивание'), (apps.yandex.consts.Mode['ASPIC'], 'ASPIC. Холодец'), (apps.yandex.consts.Mode['BODY_FOOD'], 'BODY_FOOD. Детское питание'), (apps.yandex.consts.Mode['BAKING'], 'BAKING. Выпечка'), (apps.yandex.consts.Mode['BREAD'], 'BREAD. Хлеб'), (apps.yandex.consts.Mode['BOOLING'], 'BOOLING. Варка'), (apps.yandex.consts.Mode['CEREALS'], 'CEREALS. Крупы'), (apps.yandex.consts.Mode['CHEESECAKE'], 'CHEESECAKE. Чизкейк'), (apps.yandex.consts.Mode['DEEP_FRYER'], 'DEEP_FRYER. Фритюр'), (apps.yandex.consts.Mode['DESSERT'], 'DESSERT. Десерты'), (apps.yandex.consts.Mode['FOWL'], 'FOWL. Дичь'), (apps.yandex.consts.Mode['FRYING'], 'FRYING. Жарка'), (apps.yandex.consts.Mode['MACARONI'], 'MACARONI. Макароны'), (apps.yandex.consts.Mode['MILK_PORRIDGE'], 'MILK_PORRIDGE. Молочная каша'), (apps.yandex.consts.Mode['MULTICOOKER'], 'MULTICOOKER. Мультиповар'), (apps.yandex.consts.Mode['PASTA'], 'PASTA. Паста'), (apps.yandex.consts.Mode['PILAF'], 'PILAF. Плов'), (apps.yandex.consts.Mode['PIZZA'], 'PIZZA. Пицца'), (apps.yandex.consts.Mode['SAUCE'], 'SAUCE. Соус'), (apps.yandex.consts.Mode['SLOW_COOK'], 'SLOW_COOK. Томление'), (apps.yandex.consts.Mode['SOUP'], 'SOUP. Суп'), (apps.yandex.consts.Mode['STEAM'], 'STEAM. Пар'), (apps.yandex.consts.Mode['STEWING'], 'STEWING. Тушение'), (apps.yandex.consts.Mode['VACUUM'], 'VACUUM. Вакуум'), (apps.yandex.consts.Mode['YOGURT'], 'YOGURT. Йогурт')], max_length=50, verbose_name='mode'), blank=True, size=None)),
                ('split', models.BooleanField(blank=True, help_text='За включение/выключение устройства у провайдера отвечают разные команды', verbose_name='split')),
                ('range_instance', models.CharField(blank=True, choices=[(apps.yandex.consts.RangeInstance['BRIGHTNESS'], 'BRIGHTNESS. Изменение яркости световых элементов'), (apps.yandex.consts.RangeInstance['CHANNEL'], 'CHANNEL. Изменение канала, например телевизионного'), (apps.yandex.consts.RangeInstance['HUMIDITY'], 'HUMIDITY. Изменение влажности'), (apps.yandex.consts.RangeInstance['OPEN'], 'OPEN. Открывание чего-либо (открывание штор, окна)'), (apps.yandex.consts.RangeInstance['TEMPERATURE'], 'TEMPERATURE. Изменение температуры. Может обозначать температуру нагрева чайника, обогревателя или температуру кондиционера в каком-либо его режиме'), (apps.yandex.consts.RangeInstance['VOLUME'], 'VOLUME. Изменение громкости устройства')], max_length=50, verbose_name='instance')),
                ('unit', models.CharField(blank=True, choices=[(apps.yandex.consts.RangeUnit['PERCENT'], 'Проценты'), (apps.yandex.consts.RangeUnit['CELSIUS'], 'Цельсий'), (apps.yandex.consts.RangeUnit['KELVIN'], 'Кельвины')], max_length=50, verbose_name='Единица измерения')),
                ('random_access', models.BooleanField(blank=True, help_text='Если эта возможность выключена, пользователю будет доступно только последовательное изменение значений — в большую или меньшую сторону. Например, изменение громкости телевизора при работе через ИК пульт.', verbose_name='Произвольные значения')),
                ('range_min', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Минимальное значение')),
                ('range_max', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Максимальное значение')),
                ('range_precision', models.PositiveIntegerField(blank=True, null=True, verbose_name='Шаг')),
                ('toggle_instance', models.CharField(blank=True, choices=[(apps.yandex.consts.ToggleInstance['BACKLIGHT'], 'BACKLIGHT. Подсветка'), (apps.yandex.consts.ToggleInstance['CONTROLS_LOCKED'], 'CONTROLS_LOCKED. Детский режим'), (apps.yandex.consts.ToggleInstance['IONIZATION'], 'IONIZATION. Ионизация'), (apps.yandex.consts.ToggleInstance['KEEP_WARM'], 'KEEP_WARM. Поддержание тепла'), (apps.yandex.consts.ToggleInstance['MUTE'], 'MUTE. Выключение звука'), (apps.yandex.consts.ToggleInstance['OSCILLATION'], 'OSCILLATION. Вращение'), (apps.yandex.consts.ToggleInstance['PAUSE'], 'PAUSE. Пауза')], max_length=50, verbose_name='instance')),
                ('protocol', models.CharField(blank=True, choices=[(apps.yandex.consts.Protocol['HLS'], 'HLS'), (apps.yandex.consts.Protocol['PROGRESSIVE_MP4'], 'PROGRESSIVE_MP4')], max_length=50, verbose_name='Протокол')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Возможность',
                'verbose_name_plural': 'Возможности',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Комната')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('type', models.CharField(choices=[(apps.yandex.consts.DeviceType['LIGHT'], 'LIGHT. Устройство, которое имеет управляемые светящиеся элементы'), (apps.yandex.consts.DeviceType['SOCKET'], 'SOCKET. Розетка'), (apps.yandex.consts.DeviceType['SWITCH'], 'SWITCH. Выключатель'), (apps.yandex.consts.DeviceType['THERMOSTAT'], 'THERMOSTAT. Устройство с возможностью регулирования температуры'), (apps.yandex.consts.DeviceType['THERMOSTAT_AC'], 'THERMOSTAT_AC. Устройство, управляющее микроклиматом в помещении, с возможностью регулирования температуры и режима работы'), (apps.yandex.consts.DeviceType['MEDIA_DEVICE'], 'MEDIA_DEVICE. Аудио, видео, мультимедиа техника. Устройства, которые умеют воспроизводить звук и видео. Аудио, видео, мультимедиа техника. Устройства, которые умеют воспроизводить звук и видео'), (apps.yandex.consts.DeviceType['TV'], 'TV. Устройство для просмотра видеоконтента. На устройстве можно изменять громкость и переключать каналы'), (apps.yandex.consts.DeviceType['TV_BOX'], 'TV_BOX. Устройство, подключаемое к телевизору или дисплею, для просмотра видеоконтента. На устройстве можно управлять громкостью воспроизведения и переключать каналы'), (apps.yandex.consts.DeviceType['RECEIVER'], 'RECEIVER. Устройство, подключаемое к телевизору или дисплею, для просмотра видеоконтента. На устройстве можно изменять громкость, переключать каналы и источники аудио-/видеосигнала'), (apps.yandex.consts.DeviceType['COOKING'], 'COOKING. Различная умная кухонная техника'), (apps.yandex.consts.DeviceType['COFFEE_MAKER'], 'COFFEE_MAKER. Устройство, которое умеет делать кофе'), (apps.yandex.consts.DeviceType['KETTLE'], 'KETTLE. Устройство, которое умеет кипятить воду и/или делать чай.'), (apps.yandex.consts.DeviceType['MULTICOOKER'], 'MULTICOOKER. Устройство, которое выполняет функции мультиварки — приготовление пищи по заданным программам'), (apps.yandex.consts.DeviceType['OPENABLE'], 'OPENABLE. Устройство, которое умеет открываться и/или закрываться'), (apps.yandex.consts.DeviceType['CURTAIN'], 'CURTAIN. Устройство, которое выполняет функцию штор'), (apps.yandex.consts.DeviceType['HUMIDIFIER'], 'HUMIDIFIER. Устройство, которое умеет изменять влажность в помещении'), (apps.yandex.consts.DeviceType['PURIFIER'], 'PURIFIER. Устройство с функцией очистки воздуха'), (apps.yandex.consts.DeviceType['VACUUM_CLEANER'], 'VACUUM_CLEANER. Устройство, которое выполняет функцию пылесоса'), (apps.yandex.consts.DeviceType['WASHING_MASHINE'], 'WASHING_MASHINE. Устройство для стирки белья'), (apps.yandex.consts.DeviceType['DISHWASHER'], 'DISHWASHER. Устройство для мытья посуды'), (apps.yandex.consts.DeviceType['IRON'], 'IRON. Устройство, которое выполняет функции утюга'), (apps.yandex.consts.DeviceType['SENSOR'], 'SENSOR. Устройство, которое передает данные со свойств'), (apps.yandex.consts.DeviceType['OTHER'], 'OTHER. Остальные устройства, не подходящие под типы выше')], help_text='https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html', max_length=50, verbose_name='Тип')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='Описание')),
                ('custom_data', models.JSONField(blank=True, default=dict, verbose_name='Кастомные данные')),
                ('capabilities', models.ManyToManyField(to='yandex.capability', verbose_name='Возможности')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='yandex.room', verbose_name='Комната')),
            ],
            options={
                'verbose_name': 'Устройство',
                'verbose_name_plural': 'Устройства',
            },
        ),
    ]
