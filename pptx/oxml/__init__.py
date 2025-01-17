# encoding: utf-8

"""
Initializes lxml parser and makes available a handful of functions that wrap
its typical uses.
"""

from __future__ import absolute_import

from lxml import etree

from .ns import NamespacePrefixedTag


# configure etree XML parser -------------------------------
element_class_lookup = etree.ElementNamespaceClassLookup()
oxml_parser = etree.XMLParser(remove_blank_text=True)
oxml_parser.set_element_class_lookup(element_class_lookup)


def parse_xml(xml):
    """
    Return root lxml element obtained by parsing XML character string in
    *xml*, which can be either a Python 2.x string or unicode.
    """
    root_element = etree.fromstring(xml, oxml_parser)
    return root_element


def register_element_cls(nsptagname, cls):
    """
    Register *cls* to be constructed when the oxml parser encounters an
    element having name *nsptag_name*. *nsptag_name* is a string of the form
    ``nspfx:tagroot``, e.g. ``'w:document'``.
    """
    nsptag = NamespacePrefixedTag(nsptagname)
    namespace = element_class_lookup.get_namespace(nsptag.nsuri)
    namespace[nsptag.local_part] = cls


from .chart.axis import (
    CT_AxisUnit, CT_CatAx, CT_LblOffset, CT_Scaling, CT_TickLblPos,
    CT_TickMark, CT_ValAx
)
register_element_cls('c:catAx',         CT_CatAx)
register_element_cls('c:lblOffset',     CT_LblOffset)
register_element_cls('c:majorTickMark', CT_TickMark)
register_element_cls('c:majorUnit',     CT_AxisUnit)
register_element_cls('c:minorTickMark', CT_TickMark)
register_element_cls('c:minorUnit',     CT_AxisUnit)
register_element_cls('c:scaling',       CT_Scaling)
register_element_cls('c:tickLblPos',    CT_TickLblPos)
register_element_cls('c:valAx',         CT_ValAx)


from .chart.chart import (
    CT_Chart, CT_ChartSpace, CT_ExternalData, CT_PlotArea, CT_Style
)
register_element_cls('c:chart',        CT_Chart)
register_element_cls('c:chartSpace',   CT_ChartSpace)
register_element_cls('c:externalData', CT_ExternalData)
register_element_cls('c:plotArea',     CT_PlotArea)
register_element_cls('c:style',        CT_Style)


from .chart.legend import CT_Legend, CT_LegendPos
register_element_cls('c:legend',    CT_Legend)
register_element_cls('c:legendPos', CT_LegendPos)


from .chart.plot import (
    CT_Area3DChart, CT_AreaChart, CT_BarChart, CT_BarDir, CT_DLblPos,
    CT_DLbls, CT_GapAmount, CT_Grouping, CT_LineChart, CT_Overlap,
    CT_PieChart
)
register_element_cls('c:area3DChart', CT_Area3DChart)
register_element_cls('c:areaChart',   CT_AreaChart)
register_element_cls('c:barChart',    CT_BarChart)
register_element_cls('c:barDir',      CT_BarDir)
register_element_cls('c:dLblPos',     CT_DLblPos)
register_element_cls('c:dLbls',       CT_DLbls)
register_element_cls('c:gapWidth',    CT_GapAmount)
register_element_cls('c:grouping',    CT_Grouping)
register_element_cls('c:lineChart',   CT_LineChart)
register_element_cls('c:overlap',     CT_Overlap)
register_element_cls('c:pieChart',    CT_PieChart)


from .chart.series import CT_SeriesComposite, CT_StrVal_NumVal_Composite
register_element_cls('c:pt',  CT_StrVal_NumVal_Composite)
register_element_cls('c:ser', CT_SeriesComposite)


from .chart.shared import (
    CT_Boolean, CT_Double, CT_Layout, CT_LayoutMode, CT_ManualLayout,
    CT_NumFmt, CT_UnsignedInt
)
register_element_cls('c:autoUpdate',       CT_Boolean)
register_element_cls('c:delete',           CT_Boolean)
register_element_cls('c:idx',              CT_UnsignedInt)
register_element_cls('c:invertIfNegative', CT_Boolean)
register_element_cls('c:layout',           CT_Layout)
register_element_cls('c:manualLayout',     CT_ManualLayout)
register_element_cls('c:max',              CT_Double)
register_element_cls('c:min',              CT_Double)
register_element_cls('c:numFmt',           CT_NumFmt)
register_element_cls('c:order',            CT_UnsignedInt)
register_element_cls('c:overlay',          CT_Boolean)
register_element_cls('c:smooth',           CT_Boolean)
register_element_cls('c:varyColors',       CT_Boolean)
register_element_cls('c:x',                CT_Double)
register_element_cls('c:xMode',            CT_LayoutMode)


from .dml.color import (
    CT_HslColor, CT_Percentage, CT_PresetColor, CT_SchemeColor,
    CT_ScRgbColor, CT_SRgbColor, CT_SystemColor
)
register_element_cls('a:hslClr',    CT_HslColor)
register_element_cls('a:lumMod',    CT_Percentage)
register_element_cls('a:lumOff',    CT_Percentage)
register_element_cls('a:alpha',     CT_Percentage)
register_element_cls('a:prstClr',   CT_PresetColor)
register_element_cls('a:schemeClr', CT_SchemeColor)
register_element_cls('a:scrgbClr',  CT_ScRgbColor)
register_element_cls('a:srgbClr',   CT_SRgbColor)
register_element_cls('a:sysClr',    CT_SystemColor)


from .dml.fill import (
    CT_Blip, CT_BlipFillProperties, CT_GradientFillProperties,
    CT_GroupFillProperties, CT_NoFillProperties, CT_PatternFillProperties,
    CT_RelativeRect, CT_SolidColorFillProperties
)
register_element_cls('a:blip',      CT_Blip)
register_element_cls('a:blipFill',  CT_BlipFillProperties)
register_element_cls('a:gradFill',  CT_GradientFillProperties)
register_element_cls('a:grpFill',   CT_GroupFillProperties)
register_element_cls('a:noFill',    CT_NoFillProperties)
register_element_cls('a:pattFill',  CT_PatternFillProperties)
register_element_cls('a:solidFill', CT_SolidColorFillProperties)
register_element_cls('a:srcRect',   CT_RelativeRect)


from .parts.coreprops import CT_CoreProperties
register_element_cls('cp:coreProperties', CT_CoreProperties)


from .parts.presentation import (
    CT_Presentation, CT_SlideId, CT_SlideIdList, CT_SlideMasterIdList,
    CT_SlideMasterIdListEntry, CT_SlideSize
)
register_element_cls('p:presentation',   CT_Presentation)
register_element_cls('p:sldId',          CT_SlideId)
register_element_cls('p:sldIdLst',       CT_SlideIdList)
register_element_cls('p:sldMasterId',    CT_SlideMasterIdListEntry)
register_element_cls('p:sldMasterIdLst', CT_SlideMasterIdList)
register_element_cls('p:sldSz',          CT_SlideSize)


from .parts.slide import CT_CommonSlideData, CT_Slide
register_element_cls('p:cSld', CT_CommonSlideData)
register_element_cls('p:sld',  CT_Slide)


from .parts.slidelayout import CT_SlideLayout
register_element_cls('p:sldLayout', CT_SlideLayout)


from .parts.slidemaster import (
    CT_SlideLayoutIdList, CT_SlideLayoutIdListEntry, CT_SlideMaster
)
register_element_cls('p:sldLayoutId',    CT_SlideLayoutIdListEntry)
register_element_cls('p:sldLayoutIdLst', CT_SlideLayoutIdList)
register_element_cls('p:sldMaster',      CT_SlideMaster)

from .parts.notes_slide import CT_NotesSlide
register_element_cls('p:notes', CT_NotesSlide)

from .shapes.autoshape import (
    CT_GeomGuide, CT_GeomGuideList, CT_NonVisualDrawingShapeProps,
    CT_PresetGeometry2D, CT_Shape, CT_ShapeNonVisual
)
register_element_cls('a:avLst',    CT_GeomGuideList)
register_element_cls('a:gd',       CT_GeomGuide)
register_element_cls('a:prstGeom', CT_PresetGeometry2D)
register_element_cls('p:cNvSpPr',  CT_NonVisualDrawingShapeProps)
register_element_cls('p:nvSpPr',   CT_ShapeNonVisual)
register_element_cls('p:sp',       CT_Shape)


from .shapes.connector import CT_Connector, CT_ConnectorNonVisual
register_element_cls('p:cxnSp',     CT_Connector)
register_element_cls('p:nvCxnSpPr', CT_ConnectorNonVisual)


from .shapes.graphfrm import (
    CT_GraphicalObject, CT_GraphicalObjectData, CT_GraphicalObjectFrame,
    CT_GraphicalObjectFrameNonVisual
)
register_element_cls('a:graphic',          CT_GraphicalObject)
register_element_cls('a:graphicData',      CT_GraphicalObjectData)
register_element_cls('p:graphicFrame',     CT_GraphicalObjectFrame)
register_element_cls('p:nvGraphicFramePr', CT_GraphicalObjectFrameNonVisual)


from .shapes.groupshape import (
    CT_GroupShape, CT_GroupShapeNonVisual, CT_GroupShapeProperties
)
register_element_cls('p:grpSp',      CT_GroupShape)
register_element_cls('p:grpSpPr',    CT_GroupShapeProperties)
register_element_cls('p:nvGrpSpPr',  CT_GroupShapeNonVisual)
register_element_cls('p:spTree',     CT_GroupShape)

from .shapes.cust_geom import (
    CT_CustomGeometry2D, CT_Path2DList, CT_Path2D, CT_Path2DMoveTo,
    CT_Path2DLineTo, CT_Path2DCubicBezierTo, CT_Path2DClose, CT_AdjPoint2D,
    CT_Path2DArcTo
)
register_element_cls('a:custGeom',   CT_CustomGeometry2D)
register_element_cls('a:pathLst',    CT_Path2DList)
register_element_cls('a:path',       CT_Path2D)
register_element_cls('a:moveTo',     CT_Path2DMoveTo)
register_element_cls('a:lnTo',       CT_Path2DLineTo)
register_element_cls('a:cubicBezTo', CT_Path2DCubicBezierTo)
register_element_cls('a:arcTo',      CT_Path2DArcTo)
register_element_cls('a:close',      CT_Path2DClose)
register_element_cls('a:pt',         CT_AdjPoint2D)

from .shapes.picture import CT_Picture, CT_PictureNonVisual
register_element_cls('p:blipFill', CT_BlipFillProperties)
register_element_cls('p:nvPicPr',  CT_PictureNonVisual)
register_element_cls('p:pic',      CT_Picture)


from .shapes.shared import (
    CT_ApplicationNonVisualDrawingProps, CT_LineProperties,
    CT_PresetLineDashProperties, CT_NonVisualDrawingProps,
    CT_Placeholder, CT_Point2D, CT_PositiveSize2D,
    CT_ShapeProperties, CT_Transform2D
)
register_element_cls('a:ext',      CT_PositiveSize2D)
register_element_cls('a:ln',       CT_LineProperties)
register_element_cls('a:prstDash', CT_PresetLineDashProperties)
register_element_cls('a:off',      CT_Point2D)
register_element_cls('a:xfrm',     CT_Transform2D)
register_element_cls('c:spPr',     CT_ShapeProperties)
register_element_cls('p:cNvPr',    CT_NonVisualDrawingProps)
register_element_cls('p:nvPr',     CT_ApplicationNonVisualDrawingProps)
register_element_cls('p:ph',       CT_Placeholder)
register_element_cls('p:spPr',     CT_ShapeProperties)
register_element_cls('p:xfrm',     CT_Transform2D)



from .shapes.table import (
    CT_Table, CT_TableCell, CT_TableCellProperties, CT_TableCol,
    CT_TableGrid, CT_TableProperties, CT_TableRow
)
register_element_cls('a:gridCol', CT_TableCol)
register_element_cls('a:tbl',     CT_Table)
register_element_cls('a:tblGrid', CT_TableGrid)
register_element_cls('a:tblPr',   CT_TableProperties)
register_element_cls('a:tc',      CT_TableCell)
register_element_cls('a:tcPr',    CT_TableCellProperties)
register_element_cls('a:tr',      CT_TableRow)


from .text import (
    CT_Hyperlink, CT_RegularTextRun, CT_TextBody, CT_TextBodyProperties,
    CT_TextCharacterProperties, CT_TextField, CT_TextFont, CT_TextLineBreak,
    CT_TextNormalAutofit, CT_TextParagraph, CT_TextParagraphProperties,
    CT_TextSpacing, CT_TextSpacingPercent, CT_TextSpacingPoint
)
register_element_cls('a:bodyPr',      CT_TextBodyProperties)
register_element_cls('a:br',          CT_TextLineBreak)
register_element_cls('a:defRPr',      CT_TextCharacterProperties)
register_element_cls('a:endParaRPr',  CT_TextCharacterProperties)
register_element_cls('a:fld',         CT_TextField)
register_element_cls('a:hlinkClick',  CT_Hyperlink)
register_element_cls('a:latin',       CT_TextFont)
register_element_cls('a:lnSpc',       CT_TextSpacing)
register_element_cls('a:normAutofit', CT_TextNormalAutofit)
register_element_cls('a:r',           CT_RegularTextRun)
register_element_cls('a:p',           CT_TextParagraph)
register_element_cls('a:pPr',         CT_TextParagraphProperties)
register_element_cls('a:rPr',         CT_TextCharacterProperties)
register_element_cls('a:spcAft',      CT_TextSpacing)
register_element_cls('a:spcBef',      CT_TextSpacing)
register_element_cls('a:spcPct',      CT_TextSpacingPercent)
register_element_cls('a:spcPts',      CT_TextSpacingPoint)
register_element_cls('a:txBody',      CT_TextBody)
register_element_cls('c:txPr',        CT_TextBody)
register_element_cls('p:txBody',      CT_TextBody)
